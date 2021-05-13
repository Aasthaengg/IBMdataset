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

queue = deque()
queue.append((S,0,0))
visited = set()
while queue:
	n, r, d = queue.popleft()
	if n == T and r == 0:
		print(d//3)
		exit()
	nr = (r+1)%3
	for m in E[n]:
		if (m, nr) in visited: continue
		visited.add((m, nr))
		queue.append((m, nr, d+1))
print(-1)