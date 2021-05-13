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

h, w = inpl()
maze = [list(input())[:-1] for _ in range(h)]
dp = [[0] * w for _ in range(h)]
dp[0][0] = 1
for i in range(h):
    for j in range(w):
        if i == 0 and j == 0:
            continue
        left = dp[i][j-1] if j-1>=0 and maze[i][j-1] == "." else 0
        up = dp[i-1][j] if i-1>=0 and maze[i-1][j] == "." else 0
        dp[i][j] = left + up
print(dp[h-1][w-1] % mod)
# print(dp)