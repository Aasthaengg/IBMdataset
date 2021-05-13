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
LR = []
for i in range(M):
	LR.append(rl())
cnts = [0]*(N+1)
for l, r in LR:
	cnts[l-1] += 1
	cnts[r] -= 1
ans = 0
s = 0
for i in range(N):
	s += cnts[i]
	if s == M:
		ans += 1
print(ans)
