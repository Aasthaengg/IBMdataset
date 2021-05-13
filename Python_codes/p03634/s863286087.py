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
Q, K = MAP()
xy = [LIST() for _ in range(Q)]

connection = [[] for _ in range(N)]
for a, b, c in abc:
	connection[a-1].append((b-1, c))
	connection[b-1].append((a-1, c))

#print(connection)

step = [-1]*N
step[K-1] = 0
q = deque([K-1])

while q:
	p = q.pop()
	for X, C in connection[p]:
		if step[X] == -1:
			step[X] = step[p] + C
			q.append(X)

#print(step)

for x, y in xy:
	print(step[x-1] + step[y-1])


