class UnionFind:
    def __init__(self, N):
        self.parent = list(range(N))
        self.rank = [0] * N
        self.size = [1] * N

    def find(self, x):
        r = x
        while self.parent[r] != r:
            r = self.parent[r]
        while self.parent[x] != r:
            x, self.parent[x] = self.parent[x], r
        return r

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
            self.size[y] += self.size[x]
        else:
            self.parent[y] = x
            self.size[x] += self.size[y]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def get_size(self, x):
        return self.size[self.find(x)]

N, M = map(int, input().split())
uf = UnionFind(N)
for _ in range(M):
    A, B = map(int, input().split())
    uf.unite(A-1, B-1)

ans = max(uf.get_size(i) for i in range(N))
print(ans)