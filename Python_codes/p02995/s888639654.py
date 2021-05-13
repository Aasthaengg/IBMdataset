import sys, math
from collections import defaultdict, deque, Counter
from bisect import bisect_left, bisect_right
from itertools import combinations, permutations, product
from heapq import heappush, heappop
from functools import lru_cache
input = sys.stdin.readline
rs = lambda: input().strip()
ri = lambda: int(input())
rl = lambda: list(map(int, input().split()))
mod = 1000000007
sys.setrecursionlimit(1000000)

from fractions import gcd

A, B, C, D = rl()

def f(n, d):
	return n // d

b = f(B, C)+f(B, D)-f(B, C*D//gcd(C,D))
a = f(A-1, C)+f(A-1, D)-f(A-1, C*D//gcd(C,D))

print(B-A+1 - (b-a))

