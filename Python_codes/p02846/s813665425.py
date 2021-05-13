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

T1, T2 = MAP()
A1, A2 = MAP()
B1, B2 = MAP()

P = (A1-B1)*T1
Q = (A2-B2)*T2

if P+Q == 0:
	print("infinity")
	exit()
elif 0 <= P*(P+Q):
	print(0)
	exit()
else:
	a = abs(P)
	b = abs(P - (2*P+Q))
	n = a//b
	if a%b:
		print(2*n+1)
	else:
		print(2*n)
