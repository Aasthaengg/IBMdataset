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
    n,k = map(int,ipt().split())
    hq = []
    for _ in range(n):
        a,b = map(int,ipt().split())
        hpq.heappush(hq,(a,b))
    while True:
        hqa,hqb = hpq.heappop(hq)
        if hqb < k:
            k -= hqb
        else:
            print(hqa)
            exit()
    return

if __name__ == '__main__':
    main()
