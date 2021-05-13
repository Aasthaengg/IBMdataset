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
#import numpy as np
#decimal.getcontext().prec = 10

H, W = MAP()
a = [LIST() for _ in range(H)]

cnt = 0
move = []
for i in range(H):
	for j in range(W):
		if i == H-1 and j == W-1:
			print(cnt)
			for x in move:
				print(*x)
			exit()
		if i%2 == 0:
			if a[i][j]%2 and j == W-1:
				a[i][j] -= 1
				a[i+1][j] += 1	
				cnt += 1
				move.append((i+1, j+1, i+2, j+1))
			elif a[i][j]%2:
				a[i][j] -= 1
				a[i][j+1] += 1
				cnt += 1
				move.append((i+1, j+1, i+1, j+2))
		else:
			if a[i][W-j-1]%2 and j == W-1:
				a[i][W-j-1] -= 1
				a[i+1][W-j-1] += 1
				cnt += 1
				move.append((i+1, W-j, i+2, W-j))
			elif a[i][W-j-1]%2:
				a[i][W-j-1] -= 1
				a[i][W-j-2] += 1
				cnt += 1
				move.append((i+1, W-j, i+1, W-j-1))