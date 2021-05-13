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

def warshall_floyd(d,n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[j][k])

    return d

N, M, L = list(map(int, input().split()))

d = [[INF for j in range(N)] for i in range(N)]
for i in range(M):
    a, b, c = map(int,input().split())
    d[a-1][b-1] = c
    d[b-1][a-1] = c

d = warshall_floyd(d, N)

dd = [[INF for j in range(N)] for i in range(N)]
for i in range(N):
    for j in range(i+1, N):
        if d[i][j] <= L:
            dd[i][j] = 1
            dd[j][i] = 1

dd = warshall_floyd(dd, N)

Q = int(input())
for q in range(Q):
    s, t = map(int, input().split())
    ans = dd[s-1][t-1]-1
    if ans == INF-1:
        print(-1)
    else:
        print(ans)

