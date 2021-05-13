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
    for i,ai in enumerate(ipt().split()):
        a.append(int(ai)-i-1)
    a.sort()
    b = a[n//2]
    ans = 0
    for i in a:
        ans += abs(i-b)
    print(ans)


    return

if __name__ == '__main__':
    main()
