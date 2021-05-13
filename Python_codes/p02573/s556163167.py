from collections import Counter


class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)
        self.size = [1] * (n + 1)

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.par[x] > self.par[y]:
            x, y = y, x

        self.par[y] = x
        self.size[x] += self.size[y]
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1

    def same_check(self, x, y):
        return self.find(x) == self.find(y)


N, M = map(int, input().split())
uf = UnionFind(N)

for _ in range(M):
    a, b = map(int, input().split())
    uf.union(a, b)

ans = max(uf.size)

print(ans)