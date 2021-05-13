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
S = []
walls = 0
for _ in range(H):
    line = INPUT()
    walls += line.count('#')
    S.append(line)

dist = [[INF]*W for _ in range(H)]
dist[0][0] = 1
queue = deque([[0, 0]])
while queue:
    y, x = queue.popleft()
    if y == H - 1 and x == W - 1:
        print(H*W - walls - dist[y][x])
        break

    for dy, dx in [(y, x-1), (y-1, x), (y, x+1), (y+1, x)]:
        if 0 <= dy < H and 0 <= dx < W and S[dy][dx] == '.' and dist[dy][dx] == INF:
            dist[dy][dx] = dist[y][x] + 1
            queue.append([dy, dx])
else:
    print(-1)
