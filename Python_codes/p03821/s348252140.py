import math
#import numpy as np
import queue
from collections import deque,defaultdict
import heapq as hpq
from sys import stdin,setrecursionlimit
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse import csr_matrix
ipt = stdin.readline
setrecursionlimit(10**7)

def main():
    n = int(ipt())
    a = []
    b = []
    for i in range(n):
        ai,bi = map(int,ipt().split())
        a.append(ai)
        b.append(bi)
    ans = 0
    for i in range(n):
        ai = a[n-1-i]
        bi = b[n-1-i]
        pi = bi-(ai+ans-1)%bi-1
        ans += pi
    print(ans)
    return

if __name__ == '__main__':
    main()
