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

N = ri()
edges = defaultdict(list)
for i in range(N-1):
	u, v, w = rl()
	u, v = u-1, v-1
	edges[u].append((v,w))
	edges[v].append((u,w))

visited = {}
colors = [None] * N
colors[0] = 0
def dfs(node, prev=-1):
	if node in visited: return
	visited[node] = 1
	color = colors[node]
	for next_node, dist in edges[node]:
		if next_node == prev: continue
		if dist % 2 == 0:
			colors[next_node] = colors[node]
		else:
			colors[next_node] = int(not colors[node])
		dfs(next_node, node)
dfs(0)
for c in colors:
	print(c)
