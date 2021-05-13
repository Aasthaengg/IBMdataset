import sys
import numpy as np
from math import ceil as C, floor as F
from collections import defaultdict as D
 
def S(): return sys.stdin.readline().rstrip().split(' ')
def Ss(): return list(S())
def I(): return _I(S())
def Is(): return list(I())
def _I(ss): return map(int, ss) if len(ss) > 1 else int(ss[0])
 
N = I()
alp = 'abcdefghijklmnopqrstuvwxyz'
 
def get_name(n, name):
  n = n-1
  
  if n <= 25:
    return '{}{}'.format(alp[n], name)
  
  q = F(n / 26)
  r = n % 26
  return get_name(q, '{}{}'.format(alp[r], name))
 
print(get_name(N, ''))