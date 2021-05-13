from sys import stdin
import sys
import math
from functools import reduce
import functools
import itertools
from collections import deque,Counter,defaultdict
from operator import mul
import copy
# ! /usr/bin/env python
# -*- coding: utf-8 -*-
import heapq
sys.setrecursionlimit(10**6)
# INF =  float("inf")
INF = 10**18
import bisect
import statistics
mod = 10**9+7
# mod = 998244353

## a, bを無向辺として，隣接リストを作成
N, Q = list(map(int, input().split()))
al = [[] for i in range(N)]

for i in range(N-1):
    a, b = list(map(int, input().split()))

    al[a-1].append(b-1)
    al[b-1].append(a-1)

visited = [0 for i in range(N)]
seen = [0 for i in range(N)]
score = [0 for i in range(N)]

for i in range(Q):
    p, x = map(int, input().split())
    score[p-1] += x

@functools.lru_cache(None)
def dfs_rec(u):
    visited[u] = 1
    for v in al[u]:
        if visited[v] == 0:
            score[v] += score[u]
            dfs_rec(v)

dfs_rec(0)

print(" ".join(map(str, score)))