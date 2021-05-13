import math, sys
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from copy import deepcopy
from functools import lru_cache
from heapq import heapify, heappop, heappush
from itertools import accumulate, combinations, permutations
input = sys.stdin.readline
mod = 10**9 + 7
ns = lambda: input().strip()
ni = lambda: int(input().strip())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n = ni()
ans = ''
while n != 0:
    r = n % 2
    if r < 0:
        r += 2
    n = (n - r) // (-2)
    ans += str(r)
if ans == '':
    print(0)
else:
    print(ans[::-1])