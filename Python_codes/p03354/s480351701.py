import sys
input = sys.stdin.readline

class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.siz = [1] * n
    
    def root(self, x):
        if self.par[x] == x: return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]

    def size(self, x):
        self.siz[self.root(x)]

    def unite(self, x, y):
        rx, ry = self.root(x), self.root(y)
        if rx != ry:
            if self.siz[rx] < self.siz[ry]: 
                rx, ry = ry, rx
            self.par[ry] = rx
            self.siz[rx] += self.siz[ry]
    
    def same(self, x, y):
        return self.root(x) == self.root(y)

n, m = map(int, input().split())
p = list(map(int, input().split()))
uf = UnionFind(n)

for i in range(m):
    x, y = map(int, input().split())
    uf.unite(x-1, y-1)

ans = 0
for i, val in enumerate(p):
    if uf.same(i, val-1):
        ans += 1
print(ans)
