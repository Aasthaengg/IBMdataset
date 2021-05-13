import math
#import numpy as np
import queue
from collections import deque,defaultdict
import heapq
from sys import stdin,setrecursionlimit
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse import csr_matrix
ipt = stdin.readline
setrecursionlimit(10**7)

def main():
    n,k = map(int,ipt().split())
    a = [int(i) for i in ipt().split()]
    f = [int(i) for i in ipt().split()]
    a.sort()
    f.sort(reverse=True)
    l = 0
    r = 10**12
    while l < r:
        mid = l+(r-l)//2
        cst = 0
        for i in range(n):
            cst += max(0,a[i]-math.floor(mid/f[i]))
        if cst <= k:
            r = mid
        else:
            l = mid+1
    print(l)
    return

if __name__ == '__main__':
    main()
