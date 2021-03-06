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

A, B, C = MAP()

if any(x%2 for x in [A, B, C]):
	print(0)
	exit()
elif A == B == C:
	print(-1)
	exit()

cnt = 0
while 1:
	a = (B+C)/2
	b = (A+C)/2
	c = (A+B)/2
	cnt += 1
	if any(x%2 for x in [a, b, c]):
		print(cnt)
		break
	else:
		A, B, C = a, b, c

