import sys
sys.setrecursionlimit(10**8)

class UnionFind():
    def __init__(self, n):
        self.par = [-1]*n

    def find(self, x):
        if self.par[x] < 0:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        if x > y:
            x, y = y, x
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            self.par[rx] += self.par[ry]
            self.par[ry] = rx

    def size(self, x):
        return -self.par[self.find(x)]

    def same(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        return rx == ry

    def return_par(self):
        return self.par

n, m = map(int, input().split())
uf = UnionFind(n)
for i in range(m):
    a, b = map(int, input().split())
    uf.union(a-1, b-1)

ans = 0
for i in range(n):
    ans = max(ans, uf.size(i))
print(ans)
