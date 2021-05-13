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
    h,w,d = map(int,ipt().split())
    pl = [(-1,-1)]*(h*w+1)
    for i in range(h):
        a = [int(i) for i in ipt().split()]
        for j,aj in enumerate(a):
            pl[aj] = (i,j)
    ssl = [0]*(h*w+1)
    for i in range(d+1,h*w+1):
        ssl[i] = ssl[i-d]+abs(pl[i-d][0]-pl[i][0])+abs(pl[i-d][1]-pl[i][1])
    q = int(ipt())
    for _ in range(q):
        l,r = map(int,ipt().split())
        print(ssl[r]-ssl[l])

    return

if __name__ == '__main__':
    main()
