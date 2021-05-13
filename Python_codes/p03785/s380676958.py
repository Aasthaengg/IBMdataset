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
    n,c,k = map(int,ipt().split())
    t = [int(ipt()) for i in range(n)]

    t.sort()
    t0 = t[0]
    n = 1
    ans = 0
    for i in t[1::]:
        if n == c or i > k+t0:
            ans += 1
            n = 1
            t0 = i
        else:
            n += 1
    ans += 1
    print(ans)

    return

if __name__ == '__main__':
    main()
