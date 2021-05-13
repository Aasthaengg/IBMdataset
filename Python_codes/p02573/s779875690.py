class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            li = []
            while self.parents[x] >= 0:
                li.append(x)
                x = self.parents[x]
            for y in li:
                self.parents[y] = x
            return x

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

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

import sys
input = sys.stdin.buffer.readline
N,M = map(int,input().split())
uf = UnionFind(N)
for i in range(M):
    A,B = map(int,input().split())
    uf.union(A-1,B-1)
ans = 0
for i in uf.roots():
    ans = max(uf.size(i),ans)
print(ans)
