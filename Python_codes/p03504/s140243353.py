import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees, log2, gcd
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7 
#mod = 998244353
from decimal import *
import numpy as np
#decimal.getcontext().prec = 10

N, C = MAP()

n = [[] for _ in range(C)]
for _ in range(N):
	s, t, c = MAP()
	n[c-1].append((s, t))

m = [[] for _ in range(C)]

for i in range(C):
	if n[i] == []:
		continue
	n[i].sort(key = lambda y:y[0])
	s = n[i][0][0]
	t = n[i][0][1]
	L = len(n[i])
	n[i].append((0, 0))
	for j in range(L):
		if j < L and n[i][j][1] == n[i][j+1][0]:
			t = n[i][j+1][1]
		else:
			m[i].append((s, t))
			s = n[i][j+1][0]
			t = n[i][j+1][1]

#print(m)
cnt = [0]*(10**5+1)

for x in m:
	for s, t in x:
		cnt[s-1] += 1
		cnt[t] -= 1


cnt = list(accumulate(cnt))
#print(cnt)
print(max(cnt))
