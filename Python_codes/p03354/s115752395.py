class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)


N, M = map(int, input().split())
p = [0] + list(map(int, input().split()))
uf = UnionFind(N+1)
for _ in range(M):
    x, y = map(int, input().split())
    uf.unite(p[x], p[y])
ans = 0
for i in range(1, N+1):
    if uf.same(i, p[i]):
        ans += 1
print(ans)
