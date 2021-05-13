'''
研究室PCでの解答
'''
import math
#import numpy as np
import queue
import bisect
from collections import deque,defaultdict
import heapq as hpq
from sys import stdin,setrecursionlimit
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse import csr_matrix
ipt = stdin.readline
setrecursionlimit(10**7)
mod = 10**9+7 #998244353
dir = [(-1,0),(1,0),(0,-1),(0,1)]
alp = "abcdefghijklmnopqrstuvwxyz"


def main():
    n,m,p = map(int,ipt().split())

    way = [[] for i in range(n+1)]
    gway = [[] for i in range(n+1)]
    rway = [[] for i in range(n+1)]
    for i in range(m):
        a,b,c = map(int,ipt().split())
        way[a].append((b,p-c))
        rway[b].append(a)
        gway[a].append(b)

    ar = [True]*(n+1)
    ar[n] = False
    q = [n]
    while q:
        qi = q.pop()
        for j in rway[qi]:
            if ar[j]:
                ar[j] = False
                q.append(j)
    q = [1]
    ar2 = [True]*(n+1)
    ar2[1] = False
    while q:
        qi = q.pop()
        for j in gway[qi]:
            if ar2[j]:
                ar2[j] = False
                q.append(j)

    for i in range(1,n+1):
        if ar[i] or ar2[i]:
            way[i] = []

    def bellmanford(s,g,way):
        n = len(way)
        d = [10**18]*(n)
        d[s] = 0
        sl = 0
        re = True
        while re:
            re = False
            for i in range(1,n):
                for j,cj in way[i]:
                    if d[j] > d[i]+cj:
                         d[j] = d[i]+cj
                         re = True
            sl += 1
            if sl == n:
                d[g] = -10**18
                break
        return d[g]

    ans = bellmanford(1,n,way)
    if ans == -10**18:
        print(-1)
    else:
        print(max(0,-ans))

    return None

if __name__ == '__main__':
    main()
