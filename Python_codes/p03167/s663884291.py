import sys
input = sys.stdin.readline
INF = 10**18
sys.setrecursionlimit(10**6)
import itertools as it
import collections as cl
from collections import deque
import math
from functools import reduce
from collections import defaultdict
MOD = 10 ** 9 + 7

def li():
    return [int(x) for x in input().split()]


# dp[y][x]: (x, y)マスに行く経路の数

H, W = li()
maze = [list(input()) for _ in range(H)]
dp = [[0] * W for _ in range(H)]

dp[0][0] = 1

for y in range(H):
    for x in range(W):
        if maze[y][x] == '#':
            continue
        if y > 0:
            dp[y][x] += dp[y-1][x]
        if x > 0:
            dp[y][x] += dp[y][x-1]
        dp[y][x] %= MOD

print(dp[H-1][W-1])