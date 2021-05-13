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

N, T = list(map(int, input().split()))

A = []
for i in range(N):
    a, b = list(map(int, input().split()))
    A.append([a,b])

A = [0] + sorted(A, key=lambda x: x[0])
dp = [[0 for t in range(T+1)] for i in range(N+1)]
dp[0][0] = 0

for i in range(1,N+1):
    for t in range(0,T):
        if t - A[i][0] >= 0:
            dp[i][t] = max(dp[i-1][t-A[i][0]] + A[i][1], dp[i-1][t])
        else:
            dp[i][t] = dp[i-1][t]

    dp[i][T] = max(max(dp[i-1][max(0,T-A[i][0]):T]) + A[i][1], dp[i-1][T])

print(max(dp[N]))



