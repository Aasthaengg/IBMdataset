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

N, A, B, C, D = MAP()
S = list(input())

def cango(a, b):
	for i in range(a, b):
		if S[i] == "#" and S[i+1] == "#":
			return False
			break
	else:
		return True

if C < D:
	if cango(A-1, C-1) and cango(B-1, D-1):
		print("Yes")
	else:
		print("No")

else:
	for i in range(B-2, D-1):
		if S[i] == S[i+1] == S[i+2] == ".":
			S[i+1] = "#"
			break
	else:
		print("No")
		exit()

	if cango(A-1, C-1):
		print("Yes")
	else:
		print("No")