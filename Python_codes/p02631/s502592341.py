import sys
import numpy as np
from math import ceil as C, floor as F
from collections import defaultdict as D
from functools import reduce
 
alp = 'abcdefghijklmnopqrstuvwxyz'
def S(): return sys.stdin.readline().rstrip().split(' ')
def Ss(): return list(S())
def I(): return _I(S())
def Is(): return list(I())
def _I(ss): return map(int, ss) if len(ss) > 1 else int(ss[0])
 
_ = I()
xs = Is()

def xor(x, y):
  return int('{0:b}'.format(x), 2) ^ int('{0:b}'.format(y), 2)

def xors(xs):
  return reduce(xor, xs)

xxx = xors(xs)
ys = [str(xor(xxx, x)) for x in xs]
print(' '.join(ys))