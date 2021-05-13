import sys
import heapq
import re
from heapq import heapify, heappop, heappush
from itertools import permutations
from bisect import bisect_left, bisect_right
from collections import Counter, deque
from fractions import gcd
from math import factorial, sqrt, ceil
from functools import lru_cache, reduce
INF = 1 << 60
MOD = 1000000007
sys.setrecursionlimit(10 ** 7)

# ここから書き始める
n = int(input())
ans = ""
cnt = 0
if n == 0:
    print(0)
else:
    while True:
        if n == (-2) ** cnt:
            ans += "1"
            break
        if n % (-2) ** (cnt + 1) == 0:
            ans += "0"
        else:
            ans += "1"
            n -= (-2) ** cnt
        cnt += 1
        # if cnt == 4:
        #     break
    print(ans[::-1])