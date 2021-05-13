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

S = input()

dp = [[0 for j in range(13)] for i in range(len(S)+1)]
dp[0][0] = 1
for i in range(len(S)):
    if S[i] != "?":
        k = int(S[i])
        for j in range(13):
            dp[i+1][(j*10+k)%13] = (dp[i+1][(j*10+k)%13] + dp[i][j])% mod
    else:
        for k in range(10):
            for j in range(13):
                dp[i + 1][(j * 10 + k) % 13] = (dp[i + 1][(j * 10 + k) % 13] + dp[i][j]) % mod

print(dp[len(S)][5] % mod)
