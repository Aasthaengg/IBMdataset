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
    n,x = map(int,ipt().split())
    a = [int(i) for i in ipt().split()]
    ans = 0
    if a[0]+a[1] > x:
        ans += a[0]+a[1]-x
        a[1] = max(0,x-a[0])
    for i in range(1,n-1):
        ai = a[i]
        ai1 = a[i+1]
        if ai+ai1 > x:
            ans += ai+ai1-x
            a[i+1] = x-ai
    print(ans)



    return

if __name__ == '__main__':
    main()
