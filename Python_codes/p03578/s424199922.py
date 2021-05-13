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
D = LIST()
M = INT()
T = LIST()

D_c = Counter(D)
T_c = Counter(T)

cnt = 0
for k, v in zip(T_c.keys(), T_c.values()):
    if  D_c[k] < v:
        print('NO')
        break
    else:
        cnt += 1

if cnt == len(T_c):
    print('YES')
