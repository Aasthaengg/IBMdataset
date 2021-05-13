N,M = map(int,(input().split()))
A = [0]*M
B = [0]*M
for i in range(M):
    A[i],B[i] = map(int,(input().split()))
bridge = [[] for _ in range(N)]

# UnionFind
class UnionFind:

    def __init__(self, n):
        self.par =  [-1] * n
        self.rank = [0] * n
    
    def root(self,x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def union(self, x, y):
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return
        else:
            if self.rank[x] <self.rank[y]:
                self.par[y] += self.par[x] # 負+負でsize管理 
                self.par[x] = y
            else:
                self.par[x] += self.par[y]
                self.par[y] = x
                if self.rank[x] == self.rank[y]: # 負+負でsize管理 
                    self.rank[x] += 1
    
    def is_same(self, x, y):
        return self.root(x) == self.root(y)

    def size(self, x):
        return -self.par[self.root(x)]

Tree = UnionFind(N)
isolated = N*(N-1)//2
ans = []
ans.append(isolated)
for i in range(1,M)[::-1]:
    if not Tree.is_same(A[i]-1,B[i]-1):
        isolated -= Tree.size(A[i]-1) * Tree.size(B[i]-1)
    Tree.union(A[i]-1,B[i]-1)
    ans.append(isolated)

ans.reverse()
for i in range(M):
    print(ans[i])