n, m = map(int, input().split())
class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]
        self.rank = [1]*n
        self.size = [1]*n
    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
    def unite(self, x, y):
        x = self.find(x); y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                self.parent[x] = y
                self.size[y] += self.size[x]
            else:
                self.parent[y] = x
                self.size[x] += self.size[y]
                if self.rank[x] == self.rank[y]:
                    self.rank[x] += 1
    def is_same(self, x, y):
        return self.find(x) == self.find(y)
    def group_size(self, x):
        return self.size[self.find(x)]
uf = UnionFind(n); x = []
for _ in range(m):
    a, b = map(int, input().split()); a -= 1; b -= 1
    uf.unite(a, b)
for i in range(n): x.append(uf.find(i))
print(len(set(x))-1)