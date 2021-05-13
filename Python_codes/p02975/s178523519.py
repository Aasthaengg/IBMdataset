
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

a = LIST()
C = Counter(a)
A = sorted(set(a))

if N%3 == 0:
	if len(A) == 3 and A[0]^A[1] == A[2] and len(set(C.values())) == 1:
		print("Yes")
	elif len(A) == 2 and A[0] == 0 and C[0] == N//3:
		print("Yes")
	elif len(A) == 1 and A[0] == 0:
		print("Yes")
	else:
		print("No")

elif len(A) == 1 and 0 in a:
	print("Yes")
else:
	print("No")
	
