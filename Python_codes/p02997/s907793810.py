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

m = (N-1)*(N-2)//2
if K > m:
	print(-1)
	exit()

ans = []
for i in range(1, N):
	ans.append((1, i+1))
remains = []
for i in range(1, N):
	for j in range(i+1, N):
		remains.append((i+1, j+1))
k = m-K
for i in range(k):
	ans.append(remains[i])
print(len(ans))
for p in ans:
	print(*p)
