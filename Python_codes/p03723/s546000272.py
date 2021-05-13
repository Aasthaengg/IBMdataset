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
    a,b,c = map(int,ipt().split())
    for i in range(10**18):
        if a%2 == 1 or b%2 == 1 or c%2 == 1:
            print(i)
            exit()
        elif a == b == c:
            print(-1)
            exit()
        pa = a
        pb = b
        pc = c
        a = (pb+pc)//2
        b = (pa+pc)//2
        c = (pa+pb)//2
    return

if __name__ == '__main__':
    main()
