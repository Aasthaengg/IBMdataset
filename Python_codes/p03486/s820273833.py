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
    s = list(input())
    t = list(input())
    s.sort()
    t.sort(reverse=True)
    ss = "".join(s)
    st = "".join(t)
    if ss < st:
        print("Yes")
    else:
        print("No")


    return None

if __name__ == '__main__':
    main()
