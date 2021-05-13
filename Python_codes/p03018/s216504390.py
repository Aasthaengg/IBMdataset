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

s = input()
t = ""

i = 0
while i < len(s):
	if s[i:i+2] == "BC":
		t += "D"
		i += 2
	else:
		t += s[i]
		i += 1

D_cnt = []
cnt = 0
for x in t[::-1]:
	if x == "D":
		cnt += 1
		D_cnt.append(cnt)
	elif x == "A":
		D_cnt.append(cnt)
	else:
		cnt = 0
		D_cnt.append(cnt)

D_acc = D_cnt[::-1]

ans = 0
for i in range(len(t)):
	if t[i] == "A":
		ans += D_acc[i]

print(ans)

