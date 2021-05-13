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
    h,w = map(int,ipt().split())
    a = [[int(i) for i in ipt().split()] for _ in range(h)]
    ans = []
    for i in range(h):
        for j in range(w):
            if a[i][j]&1:
                if j < w-1:
                    ans.append((i+1,j+1,i+1,j+2))
                    a[i][j+1] += 1
                elif i == h-1:
                    continue
                else:
                    ans.append((i+1,j+1,i+2,j+1))
                    a[i+1][j] += 1
    print(len(ans))
    for a1,a2,a3,a4 in ans:
        print(a1,a2,a3,a4)

    return

if __name__ == '__main__':
    main()
