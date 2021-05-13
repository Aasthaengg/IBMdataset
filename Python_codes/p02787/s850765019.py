# -*- coding: utf-8 -*-
import sys
from collections import deque
from collections import defaultdict
import heapq
import collections
import itertools
import bisect
import copy
import math
from itertools import accumulate
sys.setrecursionlimit(10**6)

# lis_of_lis = [[] for _ in range(N)]


def zz(): return list(map(int, sys.stdin.readline().split()))


def z(): return int(sys.stdin.readline())


def S(): return sys.stdin.readline()[:-1]


def C(line): return [sys.stdin.readline() for _ in range(line)]


H, N = zz()
A, B = [], []
for i in range(N):
    a, b = zz()
    A.append(a)
    B.append(b)
# B, A = zip(*sorted(zip(B, A)))

max_a = max(A)
dp = [[100000000]*(H + max_a + 1)] * (N+1)  # dp[i][j]: 魔法i種類で、HPをj減らすのに必要な魔力
#  初期化
for j in range(H):
    if (j % A[0] == 0):
        dp[0][j] = (j//A[0])*B[0]
    else:
        dp[0][j] = (j//A[0]+1)*B[0]
# print(dp)
# print()

for j in range(1, H + max_a + 1):
    for i in range(0, N):

        if(j < A[i]):
            dp[i][j] = min(dp[i-1][j], B[i])
        else:
            # if (j > 8):
            #     print(dp[i - 1][j],
            #           dp[i][j - A[i]] + B[i],
            #           dp[i-1][j-A[i]] + B[i])

            dp[i][j] = min(dp[i - 1][j],
                           dp[i][j - A[i]] + B[i],
                           dp[i-1][j-A[i]] + B[i])


# print(dp)
print(dp[N-1][H])
