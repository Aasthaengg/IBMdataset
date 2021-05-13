def examF():
    M, K = LI()
    if K>=(2**M) or (M==1 and K==1):
        ans = -1
    elif K==0:
        ans = []
        s = [i for i in range(2**M)]
        for i in range(2**M):
            ans.append(i)
            ans.append(i)
    else:
        ans = []
        ans.append(K)
        for i in range(2**M):
            if i!=K:
                ans.append(i)
        ans.append(K)
        for i in range(2**M-1,-1,-1):
            if i!=K:
                ans.append(i)
    if type(ans) is int:
        print(ans)
    else:
        print(" ".join(map(str,ans)))

import sys
import copy
import bisect
import heapq
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examF()
