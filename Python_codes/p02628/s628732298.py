import sys
import numpy as np
from math import ceil as C, floor as F
from collections import defaultdict as D
from functools import reduce as R

ALP = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alp = 'abcdefghijklmnopqrstuvwxyz'
def _X(): return sys.stdin.readline().rstrip().split(' ')
def _S(ss): return tuple(ss) if len(ss) > 1 else ss[0]
def S(): return _S(_X())
def _Ss(ss): return list(ss) if isinstance(ss, tuple) else [ss]
def Ss(): return _Ss(S())
def _I(ss): return tuple([int(s) for s in ss]) if isinstance(ss, tuple) else int(ss)
def I(): return _I(S())
def _Is(ss): return list(ss) if isinstance(ss, tuple) else [ss]
def Is(): return _Is(I())

N, K = I()
xs = sorted(Is())
print(np.sum(xs[:K]))