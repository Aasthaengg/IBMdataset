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
A = [-1]
prev_a = -float('inf')
for i in range(M):
	a = ri()
	if a-prev_a == 1:
		print(0)
		exit()
	A.append(a)
	prev_a = a
A.append(N+1)

dp = [0]*(N+5)
dp[0] = 0
dp[1] = 1
for i in range(N+5-2):
	dp[i+2] = dp[i+1] + dp[i]
ans = 1
for i in range(len(A)-1):
	ans *= dp[A[i+1]-A[i]-1]
	ans = ans % mod
print(ans)
