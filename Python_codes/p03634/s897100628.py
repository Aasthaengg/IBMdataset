import sys, re
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees#, log2
from collections import deque, defaultdict, Counter
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from fractions import gcd
from heapq import heappush, heappop, heapify
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N = INT()
abc = [LIST() for _ in range(N-1)]

graph = defaultdict(list)
for a, b, c in abc:
	graph[a-1].append((b-1, c))
	graph[b-1].append((a-1, c))

Q, K = MAP()
xy = [LIST() for _ in range(Q)]

dist = [-1]*N
dist[K-1] = 0

def dfs(node):
	for to, cost in graph[node]:
		if dist[to] == -1:
			dist[to] = dist[node] + cost
			dfs(to)

dfs(K-1)
#print(dist)

for x, y in xy:
	print(dist[x-1] + dist[y-1])
