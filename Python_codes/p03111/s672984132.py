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

N, A, B, C = MAP()

l = [INT() for _ in range(N)]

ans = INF
for x in product(range(4), repeat=N):
	tmp = 0
	bamboo = [0]*4 #[不使用、Aに使用、Bに使用、Cに使用]
	for i in range(N):
		if 0 < x[i] and bamboo[x[i]]:
			tmp += 10
		bamboo[x[i]] += l[i]

	if 0 in bamboo[1:]:
		continue

	tmp += abs(bamboo[1]-A) + abs(bamboo[2]-B) + abs(bamboo[3]-C)

	ans = min(ans, tmp)

print(ans)

