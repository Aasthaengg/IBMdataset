import sys
import math
import itertools
import collections
import heapq
import re
import numpy as np
import fractions

rr = lambda: sys.stdin.buffer.readline().rstrip()
rs = lambda: sys.stdin.buffer.readline().split()
ri = lambda: int(sys.stdin.buffer.readline())
rm = lambda: map(int, sys.stdin.buffer.readline().split())
rl = lambda: list(map(int, sys.stdin.buffer.readline().split()))

n, k = rm()
a = rl()
s = set()
b = a[0]
if k in set(a):
  print('POSSIBLE')
  exit()
if len(set(a)) == 1:
  if tuple(set(a))[0] == k:
    print('POSSIBLE')
  else:
    print('IMPOSSIBLE')
  exit()
for i in a:
  g = fractions.gcd(i, b)
  if g == 1:
    print('POSSIBLE')
    exit()
  if k % g == 0 and k <= max(i, b):
    print('POSSIBLE')
    exit()
else:
  print('IMPOSSIBLE')

  


