def examD():
    N = I()
    A = LI(); A.sort()
    d = defaultdict(int)
    cur = int(0)
    for i in A:
        d[i] +=1
    for i in d:
        cur += d[i]
    cur -= len(d)
    ans = N - cur - cur%2
    print(ans)

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
