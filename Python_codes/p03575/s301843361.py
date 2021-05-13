class UnionFind:
    def __init__(self, n=0):
        self.d = [-1]*n
        self.u = n
    def root(self, x):
        if self.d[x] < 0:
            return x
        self.d[x] = self.root(self.d[x])
        return self.d[x]
    def unite(self, x, y):
        x, y = self.root(x), self.root(y)
        if x == y:
            return False
        if x > y:
            x, y = y, x
        self.d[x] += self.d[y]
        self.d[y] = x
        self.u -= 1
        return True
    def same(self, x, y):
        return self.root(x) == self.root(y)
    def size(self, x):
        return -self.d[self.root(x)]
    def num_union(self):
        return self.u


import sys
input = sys.stdin.buffer.readline
N, M = map(int, input().split())
E = [tuple(map(lambda x:int(x)-1, input().split())) for _ in range(M)]

ans = 0
for i in range(M):
    uf = UnionFind(N)
    for j, (a, b) in enumerate(E):
        if i == j:
            continue
        uf.unite(a, b)
    if uf.num_union() != 1:
        ans += 1
print(ans)
