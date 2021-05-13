import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees, log2, log
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from fractions import gcd
from heapq import heappush, heappop
from functools import reduce
from decimal import Decimal
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10**9 + 7
from decimal import *
 
H, W = MAP()
S = [input() for _ in range(H)]

w = [[-1]*W for _ in range(H)]
h = [[-1]*W for _ in range(H)]

for i in range(H):
	cnt = 0
	for j in range(W):
		if S[i][j] == ".":
			cnt += 1
			w[i][j] = cnt
		else:
			cnt = 0
	for j in range(W-2, -1, -1):
		if S[i][j] == ".":
			w[i][j] = max(w[i][j], w[i][j+1])


for i in range(W):
	cnt = 0
	for j in range(H):
		if S[j][i] == ".":
			cnt += 1
			h[j][i] = cnt
		else:
			cnt = 0

	for j in range(H-2, -1, -1):
		if S[j][i] == ".":
			h[j][i] = max(h[j][i], h[j+1][i])


ans = 0
for i in range(H):
	for j in range(W):
		if h[i][j] != -1 and w[i][j] != -1:
			ans = max(ans, h[i][j]+w[i][j]-1)
print(ans)

