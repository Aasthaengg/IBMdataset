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

a, b, x = rm()
set_ = set()
for i in range(x):
    if a+i <= b:
        set_.add(a + i)
        set_.add(b - i)
li = sorted(list(set_))
for i in li:
    print(i)







