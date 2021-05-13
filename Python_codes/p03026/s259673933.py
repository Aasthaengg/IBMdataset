import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees, log2, gcd
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from heapq import heappush, heappop
from functools import reduce, lru_cache
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = 10**6#float('inf')
mod = 10 ** 9 + 7 
#mod = 998244353
#from decimal import *
#import numpy as np
#decimal.getcontext().prec = 10

N = INT()
ab = [LIST() for _ in range(N-1)]
c = sorted(LIST())
print(sum(c)-c[-1])

cnt = [0]*N
graph = [[] for _ in range(N)]

for a, b in ab:
	graph[a-1].append(b-1)
	graph[b-1].append(a-1)
	cnt[a-1] += 1
	cnt[b-1] += 1

ans = [0]*N

q = deque([0])
while q:
	p = q.popleft()
	ans[p] = c.pop()
	for i in graph[p]:
		if ans[i] == 0:
			q.append(i)

print(*ans)