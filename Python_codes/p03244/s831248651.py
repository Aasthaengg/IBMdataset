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
from decimal import Decimal
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10**9 + 7
 
n = INT()
v = LIST()

v1 = v[::2]
v2 = v[1::2]

def cnt(v1, v2):
	ans1 = len(v1) - Counter(v1).most_common()[0][1]

	if Counter(v1).most_common()[0][0] != Counter(v2).most_common()[0][0]:
		ans2 = len(v2) - Counter(v2).most_common()[0][1]
	else:
		if len(Counter(v2).most_common()) == 1:
			ans2 = Counter(v2).most_common()[0][1]
		else:
			ans2 = len(v2) - Counter(v2).most_common()[1][1]

	return ans1 + ans2

print(min(cnt(v1, v2), cnt(v2, v1)))