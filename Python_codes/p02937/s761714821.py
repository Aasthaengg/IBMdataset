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
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7 
#mod = 998244353
from decimal import *
#import numpy as np
#decimal.getcontext().prec = 10

s = input()
t = input()

t_kinds = set(t)
dic = defaultdict(list)

for i, char in enumerate(s, 1):
	if char in t_kinds:
		dic[char].append(i)

if len(dic.keys()) < len(t_kinds):
	print(-1)
	exit()

dic_lim = defaultdict(int)
for key in dic.keys():
	dic_lim[key] = len(dic[key])

tmp = -1
ans = 0
loop_cnt = 0
for x in t:
	idx = bisect(dic[x], tmp)
	if idx == dic_lim[x]:
		tmp = dic[x][0]
		loop_cnt += 1
	else:
		tmp = dic[x][idx]
print(len(s)*loop_cnt + tmp)

