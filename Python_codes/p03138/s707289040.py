def examA():
    T, X = LI()
    ans = T/X
    print(ans)
    return

def examB():
    N = I()
    L = LI()
    ans = "Yes"
    if max(L)*2>=sum(L):
        ans = "No"
    print(ans)
    return

def examC():
    N, M = LI()
    X = LI(); X.sort()
    x = []
    for i in range(M-1):
        x.append(X[i+1]-X[i])
    x.sort()
    ans = 0
    if N>=M:
        ans = 0
    else:
        for i in range(M-N):
            ans += x[i]
    print(ans)
    return

def examD():
    N, K = LI()
    A = LI()
    d = defaultdict(int)
    maxl = len(bin(K)) -2
    if K==0:
        print(sum(A))
        exit()
    for a in A:
        for j in range(maxl):
            if a&1==1:
                d[j] +=1
            a >>=1
            if a==0:
                break
#    print(d)
    X = 0
    d0 = defaultdict(bool)
    cur = []
    for i in range(maxl):
        c = (2**i)*(N-d[i]*2)
        cur.append(max(0,c))
    curK = [0]*(maxl+1)
    curK[maxl-1] = cur[maxl-1]
    for i in range(maxl-2, -1, -1):
        if K & (1 << i) == (1 << i):
            curK[i] += curK[i + 1] + cur[i]
        else:
            d0[i] = True
            curK[i] += curK[i + 1]
    ansC = curK[0]
#    print(cur)
#    print(curK)
    for l in range(maxl):
        if d0[l]:
            continue
        now = curK[l+1]
        for i in range(l-1, -1, -1):
            now += cur[i]
        ansC = max(ansC,now)
    ans = ansC+sum(A)
    print(ans)
    return

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

if __name__ == '__main__':
    examD()
