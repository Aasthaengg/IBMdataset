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

n, m = rm()
if n == m:
    print((math.factorial(n) * math.factorial(m) * 2) % mod)
elif abs(n-m) == 1:
    print((math.factorial(n) * math.factorial(m)) % mod)
else:
    print(0)


















