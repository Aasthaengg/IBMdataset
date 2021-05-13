from collections import defaultdict,deque
import sys, bisect, math, itertools
from functools import lru_cache
# @lru_cache(maxsize=None)
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp():
    '''
    一つの整数
    '''
    return int(input())
def inpl():
    '''
    一行に複数の整数
    '''
    return list(map(int, input().split()))

n = inp()
p = list(map(float, input().split()))
# dp[i][j]=最初のi枚のコインを投げた時に表がj枚になる確率
dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        dp[i + 1][j + 1] += dp[i][j] * p[i]  # i+1枚目が表
        dp[i + 1][j] += dp[i][j] * (1.0 - p[i])  # i枚目が裏

print(sum([dp[n][i] for i in range(math.ceil(n / 2), n + 1)]))
# for i in dp:
#     print(i)
