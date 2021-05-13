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
A = rl()

X = 0
m = 1
for i in range(N):
	X += m*A[i]
	m *= -1

B = [0] * N
B[0] = X//2
for i in range(1, N):
	B[i] = A[i-1]-B[i-1]

print(*[b*2 for b in B])