import sys
import math
import itertools
import collections
import heapq
import re
import numpy as np
from functools import reduce

rr = lambda: sys.stdin.readline().rstrip()
rs = lambda: sys.stdin.readline().split()
ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))
inf = float('inf')
mod = 10**9 + 7


h, w = rm()
s = [rr() for _ in range(h)]
x = [0, 0, 1, -1, 1, 1, -1, -1]
y = [1, -1, 0, 0, 1, -1, 1, -1]
ans = ['']*h
for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            ans[i] += '#'
        else:
            c = 0
            for dx, dy in zip(x, y):
                if 0 <= i + dx < h and 0 <= j + dy < w:
                    if s[i+dx][j+dy] == '#':
                        c += 1
            ans[i] += str(c)
for i in ans:
    print(i)




