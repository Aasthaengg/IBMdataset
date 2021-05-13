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
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7 
#mod = 998244353
from decimal import *
#import numpy as np
#decimal.getcontext().prec = 10

N, K = MAP()
A = LIST()

n = max(A+[K]).bit_length()
cnt = [[0, 0] for _ in range(n)]

for a in A:
	b = "{:b}".format(a).zfill(n)[::-1]
	for i in range(n):
		cnt[i][int(b[i])] += 1

max_X = []
for cnt_0, cnt_1 in cnt:
	if cnt_0 <= cnt_1:
		max_X.append(0)
	else:
		max_X.append(1)
max_X = max_X[::-1]     #Aのリストのみから算出た最大Xの2進数表記

k = "{:b}".format(K).zfill(n)

if len(k) == n:
	for i in range(n):
		if int(k[i]) > max_X[i]:
			break
		elif int(k[i]) < max_X[i]:
			max_X[i] = 0

X = 0
for i, p in enumerate(max_X[::-1]):
	X += 2**i*p

#print(X)
ans = 0
for a in A:
	ans += a^X

print(ans)
