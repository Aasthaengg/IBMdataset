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

N, M = map(int, input().split())
a = set()
for i in range(M):
    a.add(int(input()))

dp = [0 for i in range(N+1)]
dp[0] = 1
if 1 not in a:
    dp[1] = 1
else:
    dp[1] = 0

for i in range(2,N+1):
    if i not in a:
        dp[i] = (dp[i-1] + dp[i-2]) % mod
    else:
        dp[i] = 0

print(dp[N] % mod)