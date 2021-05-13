import sys
sys.setrecursionlimit(int(1e9))

class UnionFind():
    def __init__(self, n):
        self.p = list(range(n))
    
    def find(self, x):
        if self.p[x] == x:  return x
        self.p[x] = self.find(self.p[x])
        return self.p[x]

    def unite(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y:  self.p[x] = y

N,M = map(int, input().split())
uf = UnionFind(N)
for i in range(M):
    a,b = map(int, input().split())
    uf.unite(a-1, b-1)

ans = 0
for i in range(1, N):
    if uf.find(0) != uf.find(i):
        uf.unite(0, i)
        ans += 1

print(ans)
