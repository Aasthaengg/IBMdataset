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

n = ri()
t, a = rm()
ansv = inf
ansi = 0
for i, v in enumerate(rl()):
  if abs(a-t+v*0.006) < ansv:
    ansv = abs(a-t+v*0.006)
    ansi = i+1
print(ansi)
  
    








