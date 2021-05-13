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

N, M = rl()
A = rl()
Q = []
for i in range(M):
	b, c = rl()
	Q.append((b, c))

A.sort()
Q = sorted(Q, key=lambda x: -x[1])

ans = 0
cur = 0
for b, c in Q:
	j = bisect_left(A, c)
	if j <= cur: continue
	n = min(j-cur, b)
	ans += n*c
	cur += n
if cur < N:
	ans += sum(A[cur:])
print(ans)

