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

def main():
    n = int(ipt())
    a = [int(i) for i in ipt().split()]
    b = [int(i) for i in ipt().split()]
    c = [int(i) for i in ipt().split()]

    a.sort()
    b.sort()
    c.sort()

    sb = [0]*n
    na = 0
    for i,bi in enumerate(b):
        for j in range(na,n):
            if a[j] >= bi:
                sb[i] = j
                na = j
                break
            if j == n-1:
                na = n
                break
        if na == n:
            sb[i] = n
    ssb = [0]
    for i in sb:
        ssb.append(ssb[-1]+i)

    ans = 0
    nb = 0
    for i,ci in enumerate(c):
        for j in range(nb,n):
            if b[j] >= ci:
                ans += ssb[j]
                nb = j
                break
            if j == n-1:
                nb = n
                break
        if nb == n:
            ans += ssb[-1]
    print(ans)

    return None

if __name__ == '__main__':
    main()
