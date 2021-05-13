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

N, M = rl()
E = defaultdict(list)
for i in range(M):
	u, v = rl()
	E[u-1].append(v-1)
S, T = rl()
S -= 1
T -= 1

dp = [[float('inf')]*3 for i in range(N)]

heap = []
heappush(heap, (0, S, 0))
while heap:
	d, n, r = heappop(heap)
	if n == T and r == 0:
		continue
	#if dp[n][r] != d:
	#	continue
	nr = (d+1)%3
	for m in E[n]:
		if dp[m][nr] > d+1:
			dp[m][nr] = d+1
			heappush(heap, (d+1, m, nr))

if dp[T][0] != float('inf'):
	print(dp[T][0]//3)
else:
	print(-1)
