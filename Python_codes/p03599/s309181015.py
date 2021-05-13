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

A, B, C, D, E, F = MAP()

water = set()

for a in range(F//(100*A)+1):
	for b in range((F-100*a*A)//(100*B)+1):
		water.add(100*(a*A+b*B))

sugar = [0]*(F+1)
sugar[0] = 1
for i in range(1, F+1):
	sugar[i] = 0<(sugar[i-C]*(0<i) + sugar[i-D]*(0<i))
#print(sugar)
"""
f = F//2
sugar = [0]*(F+1)
for c in range(f//C+1):
	for d in range((f-c*C)//D+1):
		sugar[c*C+d*D] = 1
print(sugar)
"""
sugar_acc = [0]*(F+1)
tmp = 0
for i in range(F//2+1):
	if sugar[i] == 1:
		tmp = i
	sugar_acc[i] = tmp

#print(water)
#print(sugar_acc)

ans = 0
den = 0
water_ans = 0
sugar_ans = 0
water = sorted(list(water))

for water_tmp in water[1:]:
	if E == 100:
		t = min(water_tmp, F-water_tmp)
	else:
		t = min(E*water_tmp//100, F-water_tmp)

	sugar_tmp = sugar_acc[t]
	if F < sugar_tmp + water_tmp:
		continue

	if sugar_tmp == 0:
		den_tmp = 0
	else:
		den_tmp = sugar_tmp/(sugar_tmp+water_tmp)

	#print(water_tmp, sugar_tmp, den_tmp, E*water_tmp//(100-E), F-water_tmp, t)
	if den <= den_tmp:
		den = den_tmp
		water_ans = water_tmp
		sugar_ans = sugar_tmp

print(water_ans+sugar_ans, sugar_ans)
