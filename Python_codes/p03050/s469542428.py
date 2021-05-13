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
    sum = 0
    for i in range(1,10**6):
        if i**2 >= n:
            break
        if n%i == 0:
            if i < n//i-1:
                sum += n//i-1
            else:
                break
    print(sum)
    return None

if __name__ == '__main__':
    main()
