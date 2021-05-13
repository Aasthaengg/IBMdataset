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
K = []
for i in range(M):
	ks = rl()
	K.append(ks[1:])
P = rl()

def check(b):
	for i in range(M):
		if sum([b[k-1] for k in K[i]]) % 2 != P[i]:
			return False
	return True

cnt = 0
for b in product([0, 1], repeat=N):
	if check(b):
		cnt += 1
print(cnt)