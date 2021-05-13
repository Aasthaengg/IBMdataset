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

N, L = rl()

aji = [0]*N

minaji = float('inf')
for i in range(N):
	aji[i] = L+i
	if abs(minaji) > abs(aji[i]):
		minaji = aji[i]
print(sum(aji)-minaji)
