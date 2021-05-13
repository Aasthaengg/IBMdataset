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
from decimal import *
#import numpy as np
#decimal.getcontext().prec = 10

N = INT()
S1 = input()
S2 = input()

if 1 < N and S1[0] == S1[1]:
	ans = 6
	tmp = 2
	flg = 1
else:
	ans = 3
	tmp = 1
	flg = 0


while tmp < N:
	if tmp < N-1 and S1[tmp] == S1[tmp+1]:
		if flg:
			ans *= 3
		else:
			ans *= 2
		flg = 1
		tmp += 2

	else:
		if flg:
			ans *= 1
		else:
			ans *= 2
		flg = 0
		tmp += 1
	ans %= mod


print(ans)


