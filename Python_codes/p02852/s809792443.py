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
    n,m = map(int,ipt().split())
    s = input()[::-1]
    ni = 0
    me = []
    while ni < n:
        for i in range(m):
            if ni+m-i <= n and s[ni+m-i] == "0":
                ni = ni+m-i
                me.append(str(m-i))
                break
            if i == m-1:
                print(-1)
                exit()
    print(" ".join(me[::-1]))
    return

if __name__ == '__main__':
    main()
