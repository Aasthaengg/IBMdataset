class UnionFind:
    def __init__(self, n):
        self.parent = [ -1 for _ in range(n) ]
        self._size = n

    def unite(self, x, y):
        x, y = self.root(x), self.root(y)
        if x != y:
            if self.parent[y] < self.parent[x]:
                x, y = y, x
            self.parent[x] += self.parent[y]
            self.parent[y] = x
            self._size -= 1

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def root(self, x):
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.root(self.parent[x])

    def size(self, x):
        return -self.parent[self.root(x)]


N, K, L = map(int, input().split())

uf_tree1 = UnionFind(N)
uf_tree2 = UnionFind(N)

for _ in range(K):
    p, q = map(int, input().split())
    p -= 1; q -= 1;
    uf_tree1.unite(p, q)

for _ in range(L):
    r, s = map(int, input().split())
    r -= 1; s -= 1;
    uf_tree2.unite(r, s)

d = {}
for i in range(N):
    pair = (uf_tree1.root(i), uf_tree2.root(i))
    d[pair] = d.get(pair, 0) + 1

for i in range(N):
    pair = (uf_tree1.root(i), uf_tree2.root(i))
    print(d[pair], end = "")
    print("\n" if i == N-1 else " ", end = "")