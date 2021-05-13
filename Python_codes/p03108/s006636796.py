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


n, m = map(int, input().split())
ab = [ map(int, input().split()) for _ in range(m) ]

ans = []
inconv = n * (n-1) // 2
uf_tree = UnionFind(n)

for a, b in ab[::-1]:
    a -= 1; b -= 1;
    ans.append(inconv)
    if not uf_tree.same(a, b):
        x = uf_tree.size(a)
        y = uf_tree.size(b)
        uf_tree.unite(a, b)
        inconv -= x*y

print(*ans[::-1], sep="\n")