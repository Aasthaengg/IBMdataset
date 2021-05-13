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

N = INT()
X = LIST()
Y = []

for i, x in enumerate(X):
	Y.append([i, x])
Y.sort(key = lambda x: x[1])
#print(Y)
M1 = Y[N//2][1]
M2 = Y[N//2-1][1]
#print(M1, M2)
for i in range(N):
	if i >= N//2:
		Y[i][1] = M2
	else:
		Y[i][1] = M1
#print(Y)
Y.sort(key = lambda x: x[0])
#print(Y)
print(*[x[1] for x in Y], sep="\n")


