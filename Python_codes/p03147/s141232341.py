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
    h = [int(i) for i in ipt().split()]
    ans = 0
    f = True
    mih = min(h)
    for i,hi in enumerate(h):
        if hi == mih:
            f = False
        elif f:
            ans += max(0,hi-h[i+1])
        else:
            ans += max(0,hi-h[i-1])
    print(ans+mih)
    return

if __name__ == '__main__':
    main()
