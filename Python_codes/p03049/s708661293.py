import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees, log2, log
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

ans = 0
a = 0
b = 0
ba = 0

for _ in range(N):
	s = input()
	ans += s.count("AB")
	if s[0] == "B" and s[-1] == "A":
		ba += 1
	elif s[0] == "B":
		b += 1
	elif s[-1] == "A":
		a += 1

if 1 < ba:
	ans += ba-1
	ba = 1

if a != 0 or b != 0:
	if ba == 1:
		ans += min(a, b) + 1
	else:
		ans += min(a, b)

print(ans)