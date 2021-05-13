import sys
import itertools
# import numpy as np
import time

sys.setrecursionlimit(10 ** 7)

from collections import defaultdict

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

class UnionFind(object):
    def __init__(self, n = 1):
        self.link = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, x):
        if self.link[x] == x:
            return x

        # re-connect union find to make the height of tree lower
        # you can use while, but recursion makes it easier to reconnect
        self.link[x] = self.find(self.link[x])
        return self.link[x]

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return

        if self.size[x] < self.size[y]:
            x, y = y, x
        self.link[y] = x
        self.size[x] += self.size[y]
    
    def get_size(self, x):
        x = self.find(x)
        return self.size[x]

# from union_find import *

# n, m = map(int, readline().split())

# u = UnionFind(n)

# a = [0 for _ in range(m)]
# b = [0 for _ in range(m)]

# for i in range(m):
#     a[i], b[i] = map(lambda x: int(x) - 1, readline().split())

# ans = [None for _ in range(m)]

# ans[-1] = n * (n - 1) // 2

# for i in range(m - 1, 0, -1):
#     x = a[i]
#     y = b[i]
#     if u.is_same(x, y):
#         ans[i - 1] = ans[i]
#     else:
#         ans[i - 1] = ans[i] - (u.get_size(x) * u.get_size(y))
#     u.unite(x, y)

# for a in ans:
#     print(a)

N, M = map(int, input().split())
A, B = [None] * M, [None] * M
for i in range(M):
    A[i], B[i] = map(int, input().split())

uf = UnionFind(N)
ans = [None] * M
ans[M - 1] = N * (N - 1) // 2
for i in range(M - 1, 0, -1):
    x, y = A[i] - 1, B[i] - 1
    if uf.is_same(x, y):
        ans[i - 1] = ans[i]
    else:
        ans[i - 1] = ans[i] - (uf.get_size(x) * uf.get_size(y))
    uf.unite(x, y)

for a in ans:
    print(a)