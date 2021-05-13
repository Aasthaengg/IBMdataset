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
    a = [int(i) for i in ipt().split()]
    a.sort()

    if n == 2:
        print(a[1]-a[0])
        print(a[1],a[0])
    else:
        if a[1] > 0:
            ans = a[0]-a[-1]
            op = [(a[0],a[-1])]
        else:
            ans = a[-1]-a[0]
            op = [(a[-1],a[0])]
        f = True
        for i in range(1,n-2):
            if f and a[i+1] > 0:
                f = False
            if f:
                op.append((max(ans,a[i]),min(ans,a[i])))
                ans = max(ans,a[i])-min(ans,a[i])
            else:
                op.append((min(ans,a[i]),max(ans,a[i])))
                ans = min(ans,a[i])-max(ans,a[i])
        op.append((max(ans,a[n-2]),min(ans,a[n-2])))
        ans = max(ans,a[n-2])-min(ans,a[n-2])
        print(ans)
        for x,y in op:
            print(x,y)


if __name__ == '__main__':
    main()
