class UnionFind(): # 0インデックス
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]
N,M = map(int,input().split())
A,B = [],[]
for _ in range(M):
    a,b = map(int,input().split())
    A.append(a-1)
    B.append(b-1)
 
cur = N *(N-1)//2
ans = [0]*(M)
 
uf = UnionFind(N)
for i in range(M-1,-1,-1):
    ans[i] = cur
    if(uf.find(A[i]) != uf.find(B[i])):
        cur -= uf.size(A[i])*uf.size(B[i])
        uf.union(A[i],B[i])
for n in ans:
    print(n)