import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from fractions import gcd
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

def dijkstra(E, start):
    N_d = len(E)
    dist = [INF] * N_d
    dist[start] = 0
    q = [(0, start)]
    while q:
        dist_v, v = heappop(q)
        if dist[v] != dist_v:
            continue
        for u, dist_vu in E[v]:
            dist_u = dist_v + dist_vu
            if dist_u < dist[u]:
                dist[u] = dist_u
                heappush(q, (dist_u, u))
    return dist

def main():
	N, u, v = MAP()

	tree = [[] for _ in range(N)]
	for _ in range(N-1):
		A, B = MAP()
		tree[A-1].append((B-1, 1))
		tree[B-1].append((A-1, 1))

	d_t = dijkstra(tree, u-1)
	d_a = dijkstra(tree, v-1)
	# print(d_t, d_a)
	ans = -1
	for i in range(N):
		if d_t[i] <= d_a[i]:  # 青木くんより距離が近いか同じところで追いつかれる
			ans = max(ans, d_a[i])
	print(ans-1)

if __name__ == '__main__':
	main()
