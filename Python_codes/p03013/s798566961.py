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

dp = [0 for i in range(N+1)]
dp[0] = 1
dp[1] = 1

for i in range(2,N+1):
    dp[i] = dp[i-1] + dp[i-2]

ans = 1
a = -1
for i in range(M):
    b = int(input())
    c = b - a - 2
    if c < 0:
        print (0)
        sys.exit()
    else:
        ans = (ans * dp[c]) % mod
        a = b

ans = (ans * dp[N-a-1]) % mod

print(ans)