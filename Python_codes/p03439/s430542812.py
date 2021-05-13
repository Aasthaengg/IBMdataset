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

N = INT()

l = 0
r = N
print(0, flush=True)
retl = input()
if retl == "Vacant": exit()

print(N-1, flush=True)
retr = input()
if retr == "Vacant": exit()

while 1:
	m = (l+r)//2
	print(m, flush=True)
	retm = input()
	if retm == "Vacant": exit()

	if (m-l)%2 == 0 and retm == retl or (m-l)%2 == 1 and retm != retl:
		l = m
		retl = retm
	else:
		r = m
		retr = retm


