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

H, W, K = MAP()
s = [input() for _ in range(H)]

ans = [[0]*W for _ in range(H)]

tmp = 1
for y in range(H):
	for x in range(W):
		if s[y][x] == "#":
			ans[y][x] = tmp
			tmp += 1

for y in range(H):
	for x in range(1, W):
		if ans[y][x] == 0 and ans[y][x-1]!= 0:
			ans[y][x] = ans[y][x-1]

for y in range(H):
	for x in range(W-2, -1, -1):
		if ans[y][x] == 0 and ans[y][x+1]!= 0:
			ans[y][x] = ans[y][x+1]

for y in range(1, H):
	for x in range(W):
		if ans[y][x] == 0 and ans[y-1][x]!= 0:
			ans[y][x] = ans[y-1][x]

for y in range(H-2, -1, -1):
	for x in range(W):
		if ans[y][x] == 0 and ans[y+1][x]!= 0:
			ans[y][x] = ans[y+1][x]

for i in range(H):
	print(*ans[i])