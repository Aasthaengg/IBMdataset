import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
from itertools import permutations,  combinations, accumulate
from functools import *
from collections import deque, defaultdict, Counter
from heapq import heapify, heappop, heappush, heappushpop

INF = float('inf')
NIL = - 1
MOD = 10 ** 9 + 7


S = input().rstrip()
dp = [[0] * 13 for _ in range(len(S) + 1)]
dp[0][0] = 1
mul = 1  # 桁数

for i in range(len(S)):
    x = S[-(i + 1)]
    if x == '?':
        for k in range(10):
            for j in range(13):
                dp[i + 1][(mul * k + j) % 13] += dp[i][j]
                dp[i + 1][(mul * k + j) % 13] %= MOD
    else:  # 数字
        k = int(x)
        for j in range(13):
            dp[i + 1][(mul * k + j) % 13] += dp[i][j]
            dp[i + 1][(mul * k + j) % 13] %= MOD
    mul = mul * 10 % 13

print(dp[len(S)][5])
