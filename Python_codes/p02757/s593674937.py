import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import accumulate, permutations, combinations, product
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
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

def main():
	N, P = MAP()
	S = list(map(int, list(input())))

	if P == 2 or P == 5:
		ans = 0

		for i, s in enumerate(S):
			if int(s)%P == 0:
				ans += i+1
		print(ans)

	else:
		tmp = 0

		mod_cnt = [0]*P

		z = 1
		for i, n in enumerate(S[::-1]):
			tmp += n*z
			z = z * 10 % P
			mod_cnt[int(tmp)%P] += 1
		ans = 0
		for v in mod_cnt:
			ans += v*(v-1)//2
		print(ans+mod_cnt[0])


if __name__ == '__main__':
	main()
