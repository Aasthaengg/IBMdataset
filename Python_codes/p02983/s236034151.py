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

L, R = rl()

ans = float('inf')
for i in range(L, min(L+2020, R+1)):
	for j in range(i+1, min(i+2020, R+1)):
		ans = min(ans, (i*j)%2019)
print(ans)
