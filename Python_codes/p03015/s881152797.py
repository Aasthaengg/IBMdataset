import sys, math
from collections import defaultdict, deque, Counter
from bisect import bisect_left, bisect_right
from itertools import combinations, permutations, product
from heapq import heappush, heappop
from functools import lru_cache
input = sys.stdin.readline
rs = lambda: input().strip()
ri = lambda: int(input())
rl = lambda: list(map(int, input().split()))
mod = 1000000007
sys.setrecursionlimit(1000000)

L = rs()

n = len(L)
dp = [[0]*2 for i in range(n+1)]
dp[0][0] = 1

for i in range(n):
	if L[i] == '0':
		dp[i+1][0] += dp[i][0] % mod # (0,0)
		dp[i+1][1] += dp[i][1] % mod # (0,0)
		dp[i+1][1] += dp[i][1]*2 % mod # (1,0), (0,1)
	else:
		dp[i+1][1] += dp[i][0] + dp[i][1] % mod # (0,0)
		dp[i+1][0] += dp[i][0]*2 % mod # (0,1), (1,0)
		dp[i+1][1] += dp[i][1]*2 % mod # (0,1), (1,0)
print((dp[n][0]+dp[n][1])%mod)
