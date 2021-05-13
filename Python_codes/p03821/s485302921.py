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
AB = [LIST() for _ in range(N)]
A, B = [], []
for a, b in AB:
	A.append(a)
	B.append(b)

cnt = 0
for i in range(N-1, -1, -1):
	if (A[i]+cnt)%B[i] == 0:
		continue
	else:
		cnt += B[i] - (A[i]+cnt)%B[i]

print(cnt)

