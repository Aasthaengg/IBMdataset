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

def unset_nth_bit(S, j):
    # Sの右からj bit目を0にする
    return S & ~(1 << j)

def set_nth_bit(S, j):
    # Sの右からj bit目を1にする
    return S | (1 << j)

def bit(S, j):
    # Sの右からj bit目(0-indexed)
    return (S>>j)&1

N, M = map(int, input().split())

a = []
c = []
for i in range(M):
    p, q = map(int, input().split())
    a.append(p)
    c.append(list(map(int, input().split())))

dp = [[INF for j in range(1<<N)] for i in range(M+1)]
dp[0][0] = 0

for i in range(M):
    for S in range(1<<N):
        SS = S
        for cc in c[i]:
            SS = set_nth_bit(SS, cc-1)
        dp[i+1][SS] = min(dp[i+1][SS], dp[i][S] + a[i])
        dp[i+1][S] = min(dp[i+1][S], dp[i][S])

if dp[M][(1<<N)-1] == INF:
    print(-1)
else:
    print(dp[M][(1<<N)-1])