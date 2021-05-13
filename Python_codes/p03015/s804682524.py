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

L = input()
n = len(L)
L = "@" + L


dp = [[0,0] for i in range(n+1)]
dp[0][0] = 1

for i in range(n):
    if L[i+1] == "0":
        dp[i+1][0] = dp[i][0] % mod
        dp[i+1][1] = 3*dp[i][1] % mod
    else:
        dp[i+1][0] = 2*dp[i][0] % mod
        dp[i+1][1] = (dp[i][0] + 3*dp[i][1]) % mod

print((dp[n][0]+dp[n][1]) % mod)