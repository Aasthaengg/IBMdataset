import sys
import re
import queue
import collections
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext
# input = sys.stdin.readline
def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def i_row(N): return [i_input() for _ in range(N)]
def i_row_list(N): return [i_list() for _ in range(N)]
def s_input(): return input()
def s_map(): return input().split()
def s_list(): return list(s_map())
def s_row(N): return [s_input for _ in range(N)]
def s_row_str(N): return [s_list() for _ in range(N)]
def s_row_list(N): return [list(s_input()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []


def main():
	N,K= i_map()
	m = 998244353
	L = []
	R = []
	for i in range(0,K):
		tmpL,tmpR = i_map()
		L.append(tmpL)
		R.append(tmpR)

	a = []
	a.append(0)
	a.append(-1)
	for i in range(2,3*N):
		a.append(0)

	f = []
	f.append(1)

	for i in range(0,N):
		for j in range(0,K):
			a[i+L[j]] += f[i]
			a[i+R[j]+1] += -f[i]
		f.append((f[i]+a[i+1])%m)

	print(f[N-1]%m)

	return

if __name__ == '__main__':
	main()