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
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10**9 + 7
#from decimal import *


S = list(input())
K = INT()

if len(Counter(S).values()) == 1:
	print(len(S)*K//2)
	exit()

S_one = S.copy()
S_two = S*2

inner = 0
outer = 0

tmp = ""
for i, s in enumerate(S_one):
	if tmp == s:
		S_one[i] ="_"
		inner += 1
		tmp = ""
	else:
		tmp = s

tmp = ""
for i, s in enumerate(S_two):
	if tmp == s:
		S_two[i] = "_"
		outer += 1
		tmp = ""
	else:
		tmp = s

outer -= inner
print(inner+outer*(K-1))