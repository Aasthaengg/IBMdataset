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
uvw = [LIST() for _ in range(N-1)]

graph = defaultdict(list)

for u, v, w in uvw:
	graph[u-1].append((v-1, w))
	graph[v-1].append((u-1, w))

#print(graph)

color = [0]*N
color[0] = 1

def DFS(node):
	for x, w in graph[node]:
		if not color[x]:
			if w%2 == 0:
				color[x] = color[node] 
			else:
				color[x] = color[node]*(-1)
			DFS(x)

DFS(0)

for x in color:
	if x == 1:
		print(0)
	elif x == -1:
		print(1)
	else:
		print("HOGE")




