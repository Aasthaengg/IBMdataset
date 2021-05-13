import sys


class UnionFind():
    def __init__(self, n):
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


N, M = map(int, input().split())
P = list(map(int, input().split()))
uf = UnionFind(N)
for IN in sys.stdin.readlines():
    x, y = map(int, IN.split())
    x -= 1; y -= 1
    uf.union(x, y)

ans = 0
for i, p in enumerate(P):
    p -= 1
    if i == p:
        ans += 1
    else:
        if uf.find(i) == uf.find(p):
            ans += 1

print(ans)
