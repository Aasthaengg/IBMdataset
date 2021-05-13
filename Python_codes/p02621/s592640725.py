import sys
import numpy as np

def S(): return sys.stdin.readline().rstrip().split(' ')
def Ss(): return list(S())
def I(): return _I(Ss())
def Is(): return list(I())
def _I(ss): return map(int, ss) if len(ss) > 1 else int(ss[0])

a = I()
print(a + a*a + a*a*a)