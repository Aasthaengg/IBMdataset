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
    x = int(ipt())
    for i in range(10**9):
        if i*(i+1)//2 >= x:
            print(i)
            exit()

    return

if __name__ == '__main__':
    main()
