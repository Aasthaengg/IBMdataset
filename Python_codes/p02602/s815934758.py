'''
自宅用PCでの解答
'''
import math
#import numpy as np
import itertools
import queue
import bisect
from collections import deque,defaultdict
import heapq as hpq
from sys import stdin,setrecursionlimit
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse import csr_matrix
ipt = stdin.readline
setrecursionlimit(10**7)
mod = 10**9+7

def main():
    n,k = map(int,ipt().split())
    a = [int(i) for i in ipt().split()]
    for i in range(n-k):
        if a[i] < a[i+k]:
            print("Yes")
        else:
            print("No")

    return None

if __name__ == '__main__':
    main()
