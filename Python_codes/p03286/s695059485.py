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
    ans = ""
    if n == 0:
        print(0)
        exit()
    while n != 0:
        if n&1:
            ans += "1"
            n = -(n-1)//2
        else:
            ans += "0"
            n = -(n//2)
    print(ans[::-1])
    return

if __name__ == '__main__':
    main()
