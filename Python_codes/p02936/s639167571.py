import sys, math
input = sys.stdin.readline
rs = lambda: input().strip()
ri = lambda: int(input())
rl = lambda: list(map(int, input().split()))
mod = 10**9 + 7

import collections
N, Q = rl()
edges = collections.defaultdict(list)
for i in range(N-1):
	a, b = rl()
	edges[a-1].append(b-1)
	edges[b-1].append(a-1)
root_cnts = [0] * N
for i in range(Q):
	p, x = rl()
	root_cnts[p-1] += x

cnts = [0] * N

queue = collections.deque()
queue.append([0, 0, -1])

while queue:
	n, c, p = queue.pop()
	c += root_cnts[n]
	cnts[n] = c
	for m in edges[n]:
		if m == p: continue
		queue.append((m, c, n))

print(*cnts)
