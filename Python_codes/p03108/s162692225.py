# coding:utf-8

import sys
import math
import time
#import numpy as np
import collections
from collections import deque
from collections import Counter
import queue
import copy
import bisect
import heapq

#Union-Find
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

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())



#sys.setrecursionlimit(10**7)
#N, Q = map(int, input().split())
#G = [list(input()) for i in range(H)]
#INF = V * 10001
#A = [int(i) for i in input().split()]
#AB = [list(map(int, input().split())) for _ in range(K)]

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
ans = [0]*(M+1)

ans[M] = math.factorial(N) // (math.factorial(N-2) * 2)

uf = UnionFind(N)

for i in reversed(range(M)):
  if not(uf.same(AB[i][0]-1, AB[i][1]-1)):
    ans[i] = ans[i+1] - uf.size(AB[i][0]-1)*uf.size(AB[i][1]-1)
  else:
    ans[i] = ans[i+1]
  uf.union(AB[i][0]-1, AB[i][1]-1)

for i in range(M):
  print(ans[i+1])
