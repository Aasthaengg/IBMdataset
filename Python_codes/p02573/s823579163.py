class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parent = [-1 for i in range(n)]
    
    def root(self, x):
        if self.parent[x] <0:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]
    
    def same(self, x, y):
        return (self.root(x) == self.root(y))

    def union(self, x, y):
        p = self.root(x)
        q = self.root(y)
        
        if not p==q :
            if self.parent[p] > self.parent[q]:
                p,q = q,p
            self.parent[p] += self.parent[q]
            self.parent[q] = p
    
    def size(self, x):
        return -self.parent[self.root(x)]



N,M = list(map(int, input().split()))

uf = UnionFind(N)
for i in range(M):
    A,B  = list(map(int, input().split()))
    uf.union(A-1,B-1)

ans = -1
for i in range(N):
    s = uf.size(i)
    if s > ans:
        ans = s

print(ans)









