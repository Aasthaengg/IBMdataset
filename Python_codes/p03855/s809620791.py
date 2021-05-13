import collections

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.rank = [0]*(n+1)

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def are_same(self, x, y):
        return self.find(x) == self.find(y)


N, K, L = map(int, input().split())
uf1 = UnionFind(N)
for _ in range(K):
    x, y = map(int, input().split())
    uf1.unite(x, y)

uf2 = UnionFind(N)
for _ in range(L):
    x, y = map(int, input().split())
    uf2.unite(x, y)

parents = [(uf1.find(i), uf2.find(i)) for i in range(1, N+1)]
lc = collections.Counter(parents)
ans = []
for i in range(N):
    ans.append(lc[parents[i]])
print(*ans)