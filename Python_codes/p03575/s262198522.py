class UnionFind():
    def __init__(self, n):
        self._n = n
        self._table = [-1]*n
        self._rank = [0]*n

    def _root(self, x):
        stack = []
        while self._table[x] >= 0:
            stack.append(x)
            x = self._table[x]
        for y in stack:
            self._table[y] = x
        return x
    
    def unite(self, x, y):
        x, y = self._root(x), self._root(y)
        if x == y:
            return
        elif self._rank[x] > self._rank[y]:
            self._table[x] += self._table[y]
            self._table[y] = x
        else:
            self._table[y] += self._table[x]
            self._table[x] = y
            if self._rank[x] == self._rank[y]:
                self._rank[y] += 1
    
    def find(self, x, y):
        return self._root(x) == self._root(y)

    def count(self, x):
        return -self._table[self._root(x)]
    
    def __str__(self):
        return str(list(self))
    def __repr__(self):           
        return repr(list(self))
    def __iter__(self):
        return (self._root(i) for i in range(n))

n, m, *AB = map(int, open(0).read().split())
ans = 0
for i in range(m):
    uf = UnionFind(n)
    for j, (a, b) in enumerate(zip(AB[::2], AB[1::2])):
        if i == j:
            continue
        uf.unite(a-1, b-1)
    ans += len(set(uf)) != 1
print(ans)