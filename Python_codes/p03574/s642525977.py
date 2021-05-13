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
INPUT = lambda: sys.stdin.readline().rstrip()
INT = lambda: int(INPUT())
MAP = lambda: map(int, INPUT().split())
S_MAP = lambda: map(str, INPUT().split())
LIST = lambda: list(map(int, INPUT().split()))
S_LIST = lambda: list(map(str, INPUT().split()))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

H, W = MAP()
S = ['.'*(W + 2), *['.' + INPUT() + '.' for _ in range(H)], '.'*(W + 2)]

ans = ["" for _ in range(H)]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
dx = [1, 1, 0, -1, -1, -1, 0, 1]
for i in range(H):
    for j in range(W):
        if S[i+1][j+1] == '#':
            ans[i] += '#'
            continue

        cnt = 0
        for y, x in zip(dy, dx):
            if S[i+1+y][j+1+x] == '#':
                cnt += 1

        ans[i] += str(cnt)

print(*ans, sep='\n')
