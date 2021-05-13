import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy,copy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from numpy import cumsum

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

def main():
	n, m = MAP()
	a = cumsum(LIST())
	b = [x % m for x in a]
	b = [0] + b

	#ans = b.count(0)
	ans = 0
	dic = defaultdict(int)
	for x in b:
		dic[x] += 1
	for i in dic.values():
		if i >1:
			ans += i * (i-1) // 2

	print(ans)

if  __name__=='__main__':
    main()
