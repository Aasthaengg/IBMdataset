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
def dfs(n, i, a_total, b_total, c_total, a_cnt, b_cnt, c_cnt):
    if i == n:
        global ans
        if a_cnt == 0 or b_cnt == 0 or c_cnt == 0:
            return
        a_cost = abs(a - a_total) + max(0, (a_cnt - 1) * 10)
        b_cost = abs(b - b_total) + max(0, (b_cnt - 1) * 10)
        c_cost = abs(c - c_total) + max(0, (c_cnt - 1) * 10)
        cost = a_cost + b_cost + c_cost
        if ans > cost:
            ans = cost
        return
    dfs(n, i + 1, a_total + l[i], b_total, c_total, a_cnt + 1, b_cnt, c_cnt)
    dfs(n, i + 1, a_total, b_total + l[i], c_total, a_cnt, b_cnt + 1, c_cnt)
    dfs(n, i + 1, a_total, b_total, c_total + l[i], a_cnt, b_cnt, c_cnt + 1)
    dfs(n, i + 1, a_total, b_total, c_total, a_cnt, b_cnt, c_cnt)

n, a, b, c = map(int, input().split())
l = [int(input()) for i in range(n)]
ans = INF
dfs(n, 0, 0, 0, 0, 0, 0, 0)
print(ans)