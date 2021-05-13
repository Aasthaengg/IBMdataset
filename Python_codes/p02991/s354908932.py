

import sys
from collections import deque, defaultdict
import copy
import bisect
#sys.setrecursionlimit(10 ** 9)
import math
import heapq
from itertools import combinations, permutations

import sys
def input():
	return sys.stdin.readline().strip()


N, M = list(map(int, input().split()))

graph = [[] for _ in range(3*N)]

for i in range(M):
	u, v = list(map(int, input().split()))
	u -= 1
	v -= 1
	graph[u%(3*N)].append((v + N)%(3*N))
	graph[(u + N) % (3 * N)].append((v+2*N)%(3*N))
	graph[(u + 2*N) % (3 * N)].append(v % (3 * N))
S, T = list(map(int, input().split()))
S -= 1
T -= 1

dist = [1000000000000000000 for _ in range(3*N)]
que = deque([])
que.append(S)
dist[S] = 0
while len(que) > 0:
	node = que.popleft()
	for edge in graph[node]:
		if dist[edge] > dist[node] + 1:
			dist[edge] = dist[node] + 1
			que.append(edge)

if dist[T] < 100000000000000:
	print(dist[T]//3)
else:
	print(-1)