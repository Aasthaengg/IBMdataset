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
    x,y = map(int,ipt().split())
    if x < y:
        ans = y-x
    else:
        ans = x-y+2
    if x*y < 0:
        ans = min(ans,abs(abs(x)-abs(y))+1)
    elif x == 0:
        if y < 0:
            ans = abs(y)+1
    elif y == 0:
        if x > 0:
            ans = x+1
    print(ans)



    return

if __name__ == '__main__':
    main()
