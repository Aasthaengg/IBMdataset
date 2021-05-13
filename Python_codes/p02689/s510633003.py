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

_, e = I()
hs = Is()

obs = sorted([(i, h) for i, h in enumerate(hs, 1)], key=lambda x:x[1], reverse=True)
seen = D(bool)

roads = D(set)
for _ in range(e):
  a, b = I()
  roads[a].add(b)
  roads[b].add(a)
  
ans = 0
for ob in obs:
  if not seen[ob[0]]:
    if all(ob[1] > hs[r-1] for r in roads[ob[0]]):
      ans += 1
    seen[ob[0]] = True
    for r in roads[ob[0]]:
      seen[r] = True
      
print(ans)