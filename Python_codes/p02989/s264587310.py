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

N = ri()
D = rl()

D.sort()

if N % 2 == 1:
	print(0)
	exit()

d1 = D[N//2-1]
d2 = D[N//2]
if d1 == d2:
	print(0)
	exit()

print(d2-d1)
