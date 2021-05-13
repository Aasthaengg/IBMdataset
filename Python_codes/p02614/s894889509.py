import sys
import numpy as np
from math import ceil as C, floor as F, sqrt
from collections import defaultdict as D, Counter as CNT
from functools import reduce as R
 
ALP = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alp = 'abcdefghijklmnopqrstuvwxyz'
def _X(): return sys.stdin.readline().rstrip().split(' ')
def _S(ss): return tuple(ss) if len(ss) > 1 else ss[0]
def S(): return _S(_X())
def Ss(): return list(S())
def _I(ss): return tuple([int(s) for s in ss]) if isinstance(ss, tuple) else int(ss)
def I(): return _I(S())
def _Is(ss): return list(ss) if isinstance(ss, tuple) else [ss]
def Is(): return _Is(I())
def rec(h, w): return [[0] * w for i in range(h)] 

h, w, k = I()
board = []

for _ in range(h):
  s = S()
  board.append([1 if x == '#' else 0 for x in s])

ans = 0
for i in range(2 ** (h + w)):
  b = bin(i)[2:].zfill(h+w)
  s = np.sum([int(b[x // w]) * int(b[h + (x % w)]) * board[x // w][x % w] for x in range(h*w)])
  if s == k:
    ans += 1
  
print(ans)