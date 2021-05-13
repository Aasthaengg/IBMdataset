import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from bisect import bisect_left
import heapq

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N, K, L = MAP()
pq = [LIST() for _ in range(K)]
rs = [LIST() for _ in range(L)]

class UnionFind:
   def __init__(self, n):
       self.par = [i for i in range(n+1)]
       self.rank = [0] * (n+1)
   # 検索
   def find(self, x):
       if self.par[x] == x:
           return x
       else:
           self.par[x] = self.find(self.par[x])
           return self.par[x]
   # 併合
   def union(self, x, y):
       x = self.find(x)
       y = self.find(y)
       if self.rank[x] < self.rank[y]:
           self.par[x] = y
       else:
           self.par[y] = x
           if self.rank[x] == self.rank[y]:
               self.rank[x] += 1
   # 同じ集合に属するか判定
   def same_check(self, x, y):
       return self.find(x) == self.find(y)

tree_road = UnionFind(N)
tree_train = UnionFind(N)
for p, q in pq:
	tree_road.union(p, q)

for r, s in rs:
	tree_train.union(r, s)

dic = defaultdict(int)
for i in range(1, N+1):
	dic[(tree_road.find(i), tree_train.find(i))] += 1

for i in range(1, N+1):
	print(dic[(tree_road.find(i), tree_train.find(i))], end=" ")
