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
rf = lambda: map(float, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))
inf = float('inf')
mod = 10**9 + 7

s = rr()
lens = len(s)
a = int(s[0])
b = s[1:]
t = '9'*(lens-1)
if b == t:
    print((lens-1)*9+a)
else:
    print((lens-1)*9+a-1)












