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
    n,m = map(int,ipt().split())
    mod = 10**9+7
    kj = [1,1]
    for i in range(2,max(m,n)+1):
        kj.append(kj[-1]*i%mod)
    if abs(n-m) >= 2:
        print(0)
    elif abs(n-m) == 1:
        print(kj[n]*kj[m]%mod)
    else:
        print((2*kj[n]**2)%mod)

    return

if __name__ == '__main__':
    main()
