'''
自宅用PCでの解答
'''
import math
#import numpy as np
import itertools
import queue
import bisect
from collections import deque,defaultdict
import heapq as hpq
from sys import stdin,setrecursionlimit
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse import csr_matrix
ipt = stdin.readline
setrecursionlimit(10**7)
mod = 10**9+7
dir = [(-1,0),(0,-1),(1,0),(0,1)]
alp = "abcdefghijklmnopqrstuvwxyz"

def main():
    n,q = map(int,ipt().split())
    base = 10**9+1
    hq = []
    for i in range(n):
        s,t,x = map(int,ipt().split())
        if t < x:
            continue
        hpq.heappush(hq,max(0,(s-x))*2*base+x*2+1)
        hpq.heappush(hq,(t-x)*2*base+x*2)

#    print(hq)
    iv = []
    dd = dict()
    for i in range(q):
        f = True
        d = (int(ipt())+1)*2*base
        while hq and hq[0] < d:
            hi = hpq.heappop(hq)
            t = hi//(2*base)
            p = hi%2
            x = (hi//2)%base
            if p:
                dd[x] = True
                hpq.heappush(iv,x)
            else:
                dd[x] = False
        while iv:
            ii = iv[0]
            if dd[ii]:
                print(ii)
                f = False
                break
            else:
                hpq.heappop(iv)
        if f:
            print(-1)

    return None

if __name__ == '__main__':
    main()
