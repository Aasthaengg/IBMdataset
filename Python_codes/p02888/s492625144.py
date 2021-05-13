import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees#, log2, log
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from fractions import gcd
from heapq import heappush, heappop
from functools import reduce
from decimal import Decimal
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10**9 + 7
from decimal import *

N = INT()
L = LIST()

cnt = [0]*(10**3+1)
for x in L:
	cnt[x] += 1

cnt = list(accumulate(cnt))

ans = 0
for x, y in combinations(L, 2):
	ans += cnt[min(x+y-1, 1000)] - cnt[abs(x-y)] - (abs(x-y) < x < x+y) - (abs(x-y) < y < x+y)

print(ans//3)