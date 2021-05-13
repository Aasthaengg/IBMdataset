def examA():
    a, b, c = LI()
    da = b-a
    db = c-b
    if da==db:
        ans="YES"
    else:
        ans="NO"
    print(ans)


import sys
import copy
import bisect
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examA()
