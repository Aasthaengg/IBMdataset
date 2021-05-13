import sys
import math
import itertools
import collections
import heapq
import re
import numpy as np

rr = lambda: sys.stdin.readline().rstrip()
rs = lambda: sys.stdin.readline().split()
ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))
inf = float('inf')
mod = 10**9 + 7

s = rr()
a, b = int(s[:2]), int(s[2:])
if 0 < a < 13:
  if 0 < b < 13:
    print('AMBIGUOUS')
  else:
    print('MMYY')
else:
  if 0 < b < 13:
    print('YYMM')
  else:
    print('NA')




