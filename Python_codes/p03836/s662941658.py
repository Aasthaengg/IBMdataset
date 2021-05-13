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
    sx,sy,tx,ty = map(int,ipt().split())
    dx = tx-sx
    dy = ty-sy
    print("U"*dy+"R"*dx+"D"*dy+"L"*dx+"L"+"U"*(dy+1)+"R"*(dx+1)+"D"+"R"+"D"*(dy+1)+"L"*(dx+1)+"U")
    return

if __name__ == '__main__':
    main()
