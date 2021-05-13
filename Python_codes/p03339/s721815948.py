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

N = INT()
S = input()
 
tmp_W = 0
tmp_E = 0
 
cnt = [0]*len(S)
for i in range(len(S)):
	if S[i] == "W":
		tmp_W += 1
	cnt[i] += tmp_W
 
for i in range(len(S)-1, -1, -1):
	if S[i] == "E":
		tmp_E += 1
	cnt[i] += tmp_E
 
print(min(cnt)-1)