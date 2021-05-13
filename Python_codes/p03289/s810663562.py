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
if s[0] != 'A':
  print('WA')
  exit()
if 'C' in s[2:-1] and s.count('C') == 1:
  for i in s.replace('A', '').replace('C', ''):
    if 97 <= ord(i) <= 122:
      continue
    else:
      print('WA')
      exit()
  else:
    print('AC')
else:
  print('WA')














