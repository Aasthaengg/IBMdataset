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

s = rr()
lens = len(s)
for i in range(2, lens, 2):
  if s[:(lens - i) // 2] == s[(lens - i) // 2:lens - i]:
    print(lens - i)
    exit()
    















