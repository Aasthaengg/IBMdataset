import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees#, log2
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
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
mod = 10**9 + 7
#from decimal import *

N, M = MAP()
PY = [LIST() for _ in range(M)]

for i in range(M):
	PY[i].append(i)

PY.sort(key = lambda x: (x[0], x[1]))

tmp = 0
cnt = 0
for i in range(M):
	if PY[i][0] != tmp:
		cnt = 1
		tmp = PY[i][0]
	else:
		cnt += 1
	PY[i].append(str(PY[i][0]).zfill(6)+str(cnt).zfill(6))

PY.sort(key = lambda x:x[2])

print(*[PY[i][3] for i in range(M)], sep = "\n")
