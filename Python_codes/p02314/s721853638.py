import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

from collections import deque
sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces

n, m = na()
c = na()
dp = [[100000000] * (50001) for _ in range(20+1)]
for i in range(20+1):
    dp[i][0] = 0
for i in range(m):
    for j in range(n+1):
        if j >= c[i]:
            dp[i+1][j] = min(dp[i+1][j-c[i]] + 1, dp[i][j])
        else:
            dp[i+1][j] = dp[i][j]
print(dp[m][n])
