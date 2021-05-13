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
dir = [(-1,0),(0,-1),(1,0),(0,1)]
alp = "abcdefghijklmnopqrstuvwxyz"

def main():
    n,k = map(int,ipt().split())
    if k > (n-1)*(n-2)//2:
        print(-1)
    else:
        num = (n-1)*(n-2)//2-k
        print(num+(n-1))
        for i in range(2,n+1):
            print(1,i)
        for i in range(2,n+1):
            for j in range(i+1,n+1):
                if num == 0:
                    break
                print(i,j)
                num -= 1
    


    return None

if __name__ == '__main__':
    main()
