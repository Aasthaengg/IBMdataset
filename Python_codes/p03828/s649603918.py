import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians#, log2
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy, copy
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
mod = 10 ** 9 + 7
#import numpy as np
#from decimal import *

#素因数分解
def factorization(n):
	arr = []
	tmp = n
	for i in range(2, int(-(-n**0.5//1))+1):
		if tmp%i == 0:
			cnt = 0
			while tmp%i == 0:
				cnt += 1
				tmp //= i
			arr.append([i, cnt])
	if tmp != 1:
		arr.append([tmp, 1])
	if arr == []:
		arr.append([n, 1])
	return arr
	
N = INT()

if N == 1:
	print(1)
	exit()

dic = defaultdict(int)
for i in range(2, N+1):
	for key, value in factorization(i):
		dic[key] += value

#print(dic)
ans = 1
for value in dic.values():
	ans = ans*(value + 1)%mod

print(ans)
