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

N, K = rl()
V = rl()
dp = [[[-float('inf')]*(K+1) for _ in range(N+1)] for _ in range(N+1)]
dp[0][0][0] = 0

for i in range(N):
	for j in range(N):
		for k in range(K):
			dp[i][j][k+1] = max(dp[i][j][k+1], dp[i][j][k])
			# if i+j >= K or i+j >= N:
			# 	print('?', i,j,k,dp[i][j][k+1], dp[i][j][k])
			# 	dp[i][j][k+1] = max(dp[i][j][k+1], dp[i][j][k])
			# 	continue
			ni, nj, nk = i+1, j, k+1
			if ni+nj <= N:
				dp[ni][nj][nk] = max(dp[ni][nj][nk], dp[i][j][k]+V[i])
				if V[i] < 0 and nk+1 <= K:
					dp[ni][nj][nk+1] = max(dp[ni][nj][nk+1], dp[i][j][k])
			ni, nj, nk = i, j+1, k+1
			if ni+nj <= N:
				dp[ni][nj][nk] = max(dp[ni][nj][nk], dp[i][j][k]+V[N-j-1])
				if V[N-j-1] < 0 and nk+1 <= K:
					dp[ni][nj][nk+1] = max(dp[ni][nj][nk+1], dp[i][j][k])

ans = 0
for i in range(N+1):
	for j in range(N+1):
		ans = max(ans, dp[i][j][K])
print(ans)
