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

r, g, b = rm()
n = ri()
c = 0
while r >= g:
    g *= 2
    c += 1
d = 0
while g >= b:
    b *= 2
    d += 1
print('Yes' if c+d <= n else 'No')

















