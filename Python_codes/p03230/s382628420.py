'''
研究室PCでの解答
'''
import math
#import numpy as np
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
dir = [(-1,0),(1,0),(0,-1),(0,1)]
alp = "abcdefghijklmnopqrstuvwxyz"

def main():
    n = int(ipt())
    for i in range(1,10**5):
        if i*(i+1)//2 > n:
            print("No")
            exit()
        elif i*(i+1)//2 == n:
            print("Yes")
            print(i+1)
            ans = [[] for j in range(i+1)]
            ni = 1
            for j in range(i,0,-1):
                for k in range(j):
                    ans[i-j].append(ni)
                    ans[i-k].append(ni)
                    ni += 1
            for j in ans:
                print(i," ".join(map(str,j)))
            exit()

    return None

if __name__ == '__main__':
    main()
