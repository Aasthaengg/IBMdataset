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

N = ri()
W = []
for i in range(N):
	a, b = rl()
	W.append((b, a))
W.sort()

t = 0
for b, a in W:
	t += a
	if t > b:
		print('No')
		exit()
print('Yes')
