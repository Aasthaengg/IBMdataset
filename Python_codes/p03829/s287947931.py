def examD():
    N, A, B = LI()
    X = LI()
    cur = int(0)
    for i in range(N-1):
        cur += min(A*(X[i+1]-X[i]),B)
    print(cur)

import sys
import copy
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examD()