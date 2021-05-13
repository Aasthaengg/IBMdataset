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
        return self.link[x] == self.link[y]

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

n, k, l = map(int, readline().split())

u1 = UnionFind(n)
u2 = UnionFind(n)


for i in range(k):
    p, q = map(lambda x: int(x) - 1, readline().split())
    u1.unite(p, q)

for i in range(l):
    r, s = map(lambda x: int(x) - 1, readline().split())
    u2.unite(r, s)

c = defaultdict(int)

for i in range(n):
    c[(u1.find(i), u2.find(i))] += 1

for i in range(n):
    print(c[u1.find(i), u2.find(i)])
