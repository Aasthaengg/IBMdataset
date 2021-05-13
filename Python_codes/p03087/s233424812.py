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

n, q = rm()
s = rr()
cnt_li = [0]*n
for i in range(n-1):
    if s[i:i+2] == 'AC':
        cnt_li[i+1] += 1
    cnt_li[i+1] += cnt_li[i]
for _ in range(q):
    l, r = rm()
    print(cnt_li[r-1] - cnt_li[l-1])











