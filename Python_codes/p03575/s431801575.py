class UnionFind():
    def __init__(self, n):
        self.rank = [0] * n
        self.par = list(range(n))

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return
        if self.rank[rx] >= self.rank[ry]:
            self.par[ry] = rx
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1
        else:
            self.par[rx] = ry

    # find root
    def find(self, x):
        ch = []
        while self.par[x] != x:
            ch.append(x)
            x = self.par[x]
        for c in ch:
            self.par[c] = x
        return x

    def same(self, x, y):
        return self.find(x) == self.find(y)

N, M = [int(x) for x in input().split()]
E = [[int(x) - 1 for x in input().split()] for _ in range(M)]

ans = 0
for (a, b) in E:
    uf = UnionFind(N)
    for (c, d) in E: # (a, b)以外の辺でunion findを作る
        if (c, d) != (a, b):
            uf.union(c, d)
    if not uf.same(a, b):
        ans += 1

print(ans)