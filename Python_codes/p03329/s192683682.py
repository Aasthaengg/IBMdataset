import sys
import itertools
# import numpy as np
import time
import math
import heapq
from collections import defaultdict
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())
N = int(input())

coins = [(9 ** i) for i in range(1, 7)] + [(6 ** i) for i in range(1, 8)] + [1]
dp = [INF] * (N + 1)
dp[0] = 0
for i in range(len(coins)):
    for j in range(N + 1):
        if j + coins[i] > N:
            continue
        dp[j + coins[i]] = min(dp[j + coins[i]], dp[j] + 1)
print(dp[N])
