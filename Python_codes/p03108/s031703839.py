class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

n, m = map(int, input().split())
list_AB = [ list(map(int,input().split(" "))) for i in range(m)]
uf = UnionFind(n)
ans = [cmb(n, 2)]
cnt = cmb(n, 2)
for i in range(m-1, -1, -1):
    a, b = list_AB[i]
    p, q = uf.size(a-1), uf.size(b-1)
    uf.union(a-1, b-1)
    r = uf.size(a-1)
    if p != r:
        if p == 1:
            x = 0
        else:
            x = cmb(p, 2)

        if q == 1:
            y = 0
        else:
            y = cmb(q, 2)

        cnt -= cmb(r, 2) - x - y
    ans.append(cnt)

ans.reverse()
for i in range(1, m+1):
    print(ans[i])

