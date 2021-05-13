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

N, C = MAP()
stc = [LIST() for _ in range(N)]
stc.sort(key=lambda x:(x[2], x[0]))

tmp_s = stc[0][0]
tmp_t = stc[0][1]
tmp_c = stc[0][2]

stc = stc[1:]
stc_new = []

for s, t, c in stc:
	if c == tmp_c and s == tmp_t:
		tmp_t = t
	else:
		stc_new.append((tmp_s, tmp_t))
		tmp_s = s
		tmp_t = t
		tmp_c = c
stc_new.append((tmp_s, tmp_t))

now = [0]*(10**5+1)

for s, t in stc_new:
	now[s-1] += 1
	now[t] -= 1

now_acc = list(accumulate(now))

print(max(now_acc))