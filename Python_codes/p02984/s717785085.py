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
A = LIST()

a = [0] + list(accumulate(A[::2]))
b = [0] + list(accumulate(A[1::2]))

#print(a)
#print(b)

ans = []
for i in range(N):
	tmp = 0
	if i%2 == 0:
		tmp += a[-1] - a[i//2]*2
		tmp -= b[-1] - b[i//2]*2
	else:
		tmp += b[-1] - b[i//2]*2
		tmp -= a[-1] - a[(i+1)//2]*2
	ans.append(tmp)
print(*ans)