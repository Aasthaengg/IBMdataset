def examD():
    N = I()
    A = LI()
    ans = 0; l = 0; r = 0
    cur = 0
    while l < N:
        while r < N:
            if cur&A[r]==0:
                cur +=A[r]
                ans += (r-l+1)
            else:
                break
            r += 1
#        print(l,r,ans)
        cur ^=A[l]
        l +=1
    print(ans)

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examD()
