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

w, h, n = rm()
xleft = 0
xright = w
ytop = h
ybottom = 0
for _ in range(n):
  x, y, a = rm()
  if a == 1:
    xleft = max(xleft, x)
  elif a == 2:
    xright = min(xright, x)
  elif a == 4:
    ytop = min(ytop, y)
  else:
    ybottom = max(ybottom, y)
if xleft >= xright or ybottom >= ytop:
  print(0)
else:
  print((xright-xleft)*(ytop-ybottom))













