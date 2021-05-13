import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product, groupby
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

H, W = MAP()
a = [input() for _ in range(H)]
cnt = defaultdict(int)
for l in a:
	for s in l:
		cnt[s] += 1

l = sorted(list(cnt.values()), reverse=True)
if H%2==0 and W%2==0:
	for v in cnt.values():
		if v%4 != 0:
			print("No")
			break
	else:
		print("Yes")
elif H%2==0 and W%2==1:
	tmp = (W-1)*H//4
	if tmp:
		for i in range(len(l)):
			if l[i] >= 4:
				take = l[i]//4
				if tmp - take > 0:
					l[i] -= 4*take
					tmp -= take
				else:  # 取りきった
					l[i] -= 4*tmp
					tmp = 0
					break	
		else:
			print("No")
			exit()
	for v in l:
		if v%2 != 0:
			print("No")
			break
	else:
		print("Yes")
elif H%2==1 and W%2==0:
	tmp = (H-1)*W//4
	if tmp:
		for i in range(len(l)):
			if l[i] >= 4:
				take = l[i]//4
				if tmp - take > 0:
					l[i] -= 4*take
					tmp -= take
				else:  # 取りきった
					l[i] -= 4*tmp
					tmp = 0
					break	
		else:
			print("No")
			exit()
	for v in l:
		if v%2 != 0:
			print("No")
			break
	else:
		print("Yes")
else:
	tmp = (H-1)*(W-1)//4
	if tmp:
		for i in range(len(l)):
			if l[i] >= 4:
				take = l[i]//4
				if tmp - take > 0:
					l[i] -= 4*take
					tmp -= take
				else:  # 取りきった
					l[i] -= 4*tmp
					tmp = 0
					break	
		else:
			print("No")
			exit()
	odd = 0
	for v in l:
		if v%2 == 1:
			odd += 1
	print("Yes" if odd == 1 else "No")
