import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees, log2
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
xyh = [LIST() for _ in range(N)]
xyh.sort(key = lambda x:[x[0], x[1]])

for Cx in range(101):
	for Cy in range(101):
		H = 0
		H_max = INF
		for x, y, h in xyh:
			if h == 0:
				H_max = min(H_max, h + abs(x-Cx) + abs(y-Cy))
			else:
				if H == 0:
					H = h + abs(x-Cx) + abs(y-Cy)
				else:
					if H != h + abs(x-Cx) + abs(y-Cy):
						break
		else:
			if H <= H_max:
				print(Cx, Cy, H)
				break
	else:
		continue
	break

