import sys
import re
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

N = INT()
S = [input() for _ in range(N)]

new_S = []
for s in S:
    tmp = [_ for _ in s]
    tmp = ''.join(sorted(tmp))
    new_S.append(tmp)

c = Counter(new_S)

def combinations_count(n, r):
    if n < 2:
        return 0
    else:
        return factorial(n) // (factorial(n - r) * factorial(r))

ans = 0
for n in c.values():
    ans += combinations_count(n, 2)
print(ans)
