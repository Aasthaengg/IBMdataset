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
    n = int(ipt())
    a = [int(i) for i in ipt().split()]
    ans = 0
    t = 0
    pa = a[0]
    for i in a:
        if pa > i:
            if t > 0:
                t = 0
                ans += 1
            else:
                t = -1
        elif pa < i:
            if t < 0:
                t = 0
                ans += 1
            else:
                t = 1
        pa = i
    print(ans+1)

    return

if __name__ == '__main__':
    main()
