def examD():
    N = I(); A = LI()
    ans = -1; cur = []
    minA = 0; minAlocate = 0
    maxA = 0; maxAlocate = 0
    for i in range(N):
        if minA>A[i]:
            minA = A[i]; minAlocate = i
        if maxA<A[i]:
            maxA = A[i]; maxAlocate = i
    if maxA==minA==0:
        ans = 0
    elif abs(minA)<=abs(maxA):
        flag = True
        for i in range(N):
            if i!=maxAlocate:
                A[i] +=maxA
                cur.append((maxAlocate+1, i+1))
    else:
        flag = False
        for i in range(N):
            if i!=minAlocate:
                A[i] +=minA
                cur.append((minAlocate+1, i+1))
    if ans==-1:
        if flag:
            for i in range(N - 1):
                cur.append((i + 1, i + 2))
        else:
            for i in range(N-2,-1,-1):
                cur.append((i + 2, i + 1))
        print(len(cur))
        for v in cur:
            print(" ".join(map(str, v)))
    else:
        print(ans)


import sys,copy,bisect,itertools,heapq
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examD()
