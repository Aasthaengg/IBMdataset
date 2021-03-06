from collections import Counter


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.p = [e for e in range(n)]
        self.rank = [0] * n
        self.size = [1] * n

    def same(self, u, v):
        return self.find_set(u) == self.find_set(v)

    def unite(self, u, v):
        u = self.find_set(u)
        v = self.find_set(v)

        if u == v:
            return

        if self.rank[u] > self.rank[v]:
            self.p[v] = u
            self.size[u] += self.size[v]
        else:
            self.p[u] = v
            self.size[v] += self.size[u]
            if self.rank[u] == self.rank[v]:
                self.rank[v] += 1

    def find_set(self, u):
        if u != self.p[u]:
            self.p[u] = self.find_set(self.p[u])

        return self.p[u]

    def update_p(self):
        for u in range(self.n):
            self.find_set(u)

    def get_size(self, u):
        return self.size[self.find_set(u)]


n, m = map(int, input().split())
uf = UnionFind(n)
for _ in range(m):
    x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    uf.unite(x, y)

c = Counter(uf.find_set(i) for i in range(n))
ans = len(c)
print(ans)
