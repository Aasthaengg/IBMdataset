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

N, A, B = MAP()
h = [INT() for _ in range(N)]
h.sort(reverse = True)

def is_OK(T):
	H = h.copy()
	H = [x-B*T for x in h]
	tmp = 0
	for x in H:
		tmp += max(0, -(-x//(A-B)))
		if T < tmp:
			return 0
			break
	else:
		return 1
l = 0
r = -(-max(h)//B)
p = -(-l-r)//2
while l+1 != r:
	p = -(-l-r)//2
	if is_OK(p):
		r = p
	elif is_OK(p)==0:
		l = p

if is_OK(p):
	print(p)
else:
	print(p+1)
