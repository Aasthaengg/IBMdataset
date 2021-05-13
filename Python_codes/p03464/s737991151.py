import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from fractions import gcd
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

K = INT()
A = LIST()
if A[-1] != 2:
	print(-1)
	exit()

ma = 3
mi = 2

for x in A[::-1]:
	if x > ma:
		print(-1)
		exit()
	elif mi <= x <= ma:
		mi = x
		ma = 2*x-1
	else:
		tmp_mi = -(-mi//x)*x
		tmp_ma = ma//x*x
		if tmp_mi > tmp_ma:
			print(-1)
			exit()
		ma = tmp_ma+x-1
		mi = tmp_mi

print(mi, ma)
