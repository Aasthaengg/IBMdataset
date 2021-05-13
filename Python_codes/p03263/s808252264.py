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

H, W = MAP()

a = [LIST() for _ in range(H)]
cnt = 0

ans = []
for y in range(H):
	x = 0
	while x < W:
		if x < W-1 and a[y][x]%2:
			ans.append((y+1, x+1, y+1, x+2))
			cnt += 1
			a[y][x] -= 1
			a[y][x+1] += 1
		x += 1

y = 0
while y < H-1 :
	if a[y][-1]%2:
		ans.append((y+1, W, y+2, W))
		cnt += 1
		a[y][-1] -= 1
		a[y+1][-1] += 1
	y += 1

print(cnt)
for x in ans:
	print(*x)