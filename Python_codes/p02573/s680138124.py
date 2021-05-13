from sys import stdin
from collections import defaultdict
from heapq import *

class UnionFind:

    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n)]
        self.height = [0] * n
        self.size = [1] * n

    def find(self, x):
        if self.par[x] == x:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def getsize(self, x):
        return self.size[self.find(x)]

    def unite(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.height[x] < self.height[y]:
            self.par[x] = y
            self.size[y] += self.size[x]
        else:
            self.par[y] = self.par[x]
            self.size[x] += self.size[y]
            if self.height[x] == self.height[x]:
                self.height[x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

N, M = map(int, input().split())
uf = UnionFind(N+1)
for i in range(M):
    a, b = map(int, input().split())
    uf.unite(a, b)
ans = 0
for i in range(N):
    ans = max(ans, uf.getsize(i+1))
print(ans)