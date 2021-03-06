
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m = map(int, input().split())
p = list( map(int, input().split()))

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def root(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.root(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.root(x)]

    def is_same(self, x, y):
        return self.root(x) == self.root(y)

    def members(self, x):
        root = self.root(x)
        return [i for i in range(self.n) if self.root(i) == root]

    def all_roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.all_roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.all_roots()}

    def __str__(self):
        return ''.join('{}: {}'.format(r, self.members(r)) for r in self.all_roots())

uf = UnionFind(n)
ab = [tuple(map(int,input().split())) for i in range(m)]
for a,b in ab:
    a,b = a-1,b-1
    if uf.is_same(a,b): continue
    uf.union(a,b)

ans = 0

loop = [set() for i in range(n)]
for i in range(n):
    r = uf.root(i)
    loop[r].add(i)

for i in range(n):
    for j in loop[i]:
        if p[j]-1 in loop[i]: ans += 1

print(ans)
