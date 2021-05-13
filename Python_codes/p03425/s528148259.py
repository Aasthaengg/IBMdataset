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

S_head = []
for s in S:
    if s[0] in ['M', 'A', 'R', 'C', 'H']:
        S_head.append(s[0])

S_head_c = Counter(S_head)
ans = 0
for i in list(combinations(['M', 'A', 'R', 'C', 'H'], 3)):
    tmp = 1
    for j in i:
        tmp *= S_head_c[j]
    ans += tmp

print(ans)
