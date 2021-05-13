from sys import stdin
import sys
import math
from functools import reduce
import functools
import itertools
from collections import deque,Counter
from operator import mul
import copy
# ! /usr/bin/env python
# -*- coding: utf-8 -*-
import heapq
sys.setrecursionlimit(10**6)

## a, bを無向辺として，隣接リストを作成
N = int(input())
p = [0] + list(map(float, input().split()))

m = N // 2 + 1

dp = [[0.0]*(m+1) for i in range(N+1)]

dp[0][0] = 1.0
for i in range(1,N+1):
    dp[i][m] = dp[i-1][m] + dp[i-1][m-1]*p[i]
    for k in range(1,m):
        dp[i][k] = dp[i-1][k]*(1.0-p[i]) + dp[i-1][k-1]*p[i]
    dp[i][0] = dp[i-1][0]*(1.0-p[i])

print(dp[N][m])