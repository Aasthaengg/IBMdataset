import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from fractions import gcd
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7


class WeightedUnionFind:
    def __init__(self, n_nodes):
        self.n_nodes = n_nodes
        self.parents = [-1] * n_nodes
 
        # 親への重みを管理
        self.weights = [0] * n_nodes
 
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            parent = self.find(self.parents[x])
            # 親への重みを追加しながら根まで走査
            self.weights[x] += self.weights[self.parents[x]]
            self.parents[x] = parent
            return parent
 
    # xからyへの重みがw
    def unite(self, x, y, w):
        w += self.weights[x]
        w -= self.weights[y]
        x = self.find(x)
        y = self.find(y)
 
        if x == y:
            return
 
        if self.parents[x] > self.parents[y]:
            x, y = y, x
            w *= -1
 
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        self.weights[y] = w
        return
 
    def is_same(self, x, y):
        return self.find(x) == self.find(y)
 
    # xからyへの重みの取得
    def get_weight(self, x, y):
        return self.weights[y] - self.weights[x]
 
    def get_size(self, x):
        return -self.parents[self.find(x)]
 
    def get_members(self, x):
        parent = self.find(x)
        return [i for i in range(self.n_nodes) if self.find(i) == parent]
 
    def get_parent_list(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
 
    def get_n_groups(self):
        return len(self.get_parent_list())
 
    def get_members_dict(self):
        return {par: self.get_members(par) for par in self.get_parent_list()}

N, M = MAP()

tree = WeightedUnionFind(N)

for _ in range(M):
	L, R, D = MAP()
	if not tree.is_same(L-1, R-1):
		tree.unite(L-1, R-1, D)
	else:
		if not tree.get_weight(L-1, R-1) == D:
			print("No")
			break
else:
	print("Yes")
