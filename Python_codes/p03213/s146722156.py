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

n = [0]*101  #100以内の数でN!の素因数としての数

for i in range(1, N+1):
	arr = factorization(i)
	for s, t in arr:
		n[s] += t

n[1] = 0  # 1の約数は無視

C = Counter(n)
#print(C)
#print(C.items())

cnt_2_4 = 0
cnt_4_14 = 0
cnt_14_24 = 0
cnt_24_74 = 0
cnt_74 = 0
for p, q in C.items():
	if 2 <= p < 4:
		cnt_2_4 += q
	elif 4 <= p < 14:
		cnt_4_14 += q
	elif 14 <= p < 24:
		cnt_14_24 += q
	elif 24 <= p < 74:
		cnt_24_74 += q
	elif 74 <= p:
		cnt_74 += 1

cnt_24 = cnt_24_74 + cnt_74
cnt_14 = cnt_14_24 + cnt_24
cnt_4 = cnt_4_14 + cnt_14
cnt_2 = cnt_2_4 + cnt_4

ans = 0
ans += cnt_4*(cnt_4-1)//2 * (cnt_2-2)   # 5*5*3
ans += cnt_14 * (cnt_4-1)  #15*5
ans += cnt_24 * (cnt_2-1)  #25*3
ans += cnt_74  #75

print(ans)
