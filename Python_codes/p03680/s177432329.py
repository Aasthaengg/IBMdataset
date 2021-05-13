import sys
import re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, gcd
from itertools import accumulate, permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
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
A = [INT() for _ in range(N)]

r = 0
cnt = 0
flags = [0] * N
flags[0] = 1
while True:
    r = A[r] - 1
    if flags[r] == 1:
        print(-1)
        break
    else:
        flags[r] += 1
        cnt += 1

    if flags[1] == 1:
        print(cnt)
        break
