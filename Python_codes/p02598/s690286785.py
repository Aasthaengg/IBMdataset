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
mat = lambda x, y, v: [[v]*y for _ in range(x)]
ten = lambda x, y, z, v: [mat(y, z, v) for _ in range(x)]
mod = 1000000007
sys.setrecursionlimit(1000000)

N, K = rl()
A = rl()

def is_ok(x):
	s = 0
	for a in A:
		s += math.ceil(a / x)-1
	return s <= K

l, r = 0, 10**9
while r-l > 1:
	m = (r+l)//2
	if is_ok(m):
		r = m
	else:
		l = m
print(r)
