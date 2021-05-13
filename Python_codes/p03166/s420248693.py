import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product, islice
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
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')

N, M = MAP()

gout = [[] for _ in range(N)]
deg = [0]*N
for _ in range(M):
	x, y = MAP()
	gout[x-1].append(y-1)
	deg[y-1] += 1
topo = [v for v in range(N) if deg[v]==0]
path_len = [0]*N
deq = deque(topo)
ans = 0
while deq:
    v = deq.popleft()
    for t in gout[v]:
        deg[t] -= 1
        if deg[t]==0:
            deq.append(t)
            path_len[t] = path_len[v] + 1
            ans = path_len[t]

print(ans)
