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

a = ""
for _ in range(H):
	a += input()

A = Counter(a).values()
cnt_1 = 0
cnt_2 = 0
cnt_4 = 0

for x in A:
	if x%4 == 0:
		cnt_4 += 1
	elif x%2 == 0:
		cnt_2 += 1
	else:
		cnt_1 += 1

if H%2 and W%2 and cnt_1 == 1 and cnt_2 <= H//2 + W//2:
	print("Yes")
elif H%2 + W%2 == 0 and cnt_1 + cnt_2 == 0:
	print("Yes")
elif H%2 and cnt_1 == 0 and cnt_2 <= W//2:
	print("Yes")
elif W%2 and cnt_1 == 0 and cnt_2 <= H//2:
	print("Yes")
else:
	print("No")