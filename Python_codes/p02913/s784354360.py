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

N = int(input())
S = input()

dp = [[0 for j in range(N+1)] for i in range(N+1)]

for i in range(N-1,-1,-1):
    for j in range(N-1,i,-1):
        if S[i] == S[j]:
           dp[i][j] = dp[i+1][j+1] + 1
        else:
            dp[i][j] = 0

ans = 0
for i in range(N):
    for j in range(N):
        ans = max(ans, min(dp[i][j], j-i))

print(ans)