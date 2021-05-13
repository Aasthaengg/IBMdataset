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
mod = 10**9+7 #998244353
dir = [(-1,0),(1,0),(0,-1),(0,1)]
alp = "abcdefghijklmnopqrstuvwxyz"


def main():
    s = input()
#    s = "FT"*4000
    x,y = map(int,ipt().split())
#    x = 2000
#    y = 2000

    move = [[],[]]
    p = 0
    nm = 0
    for i in s:
        if i == "T":
            move[p].append(nm)
            nm = 0
            p = 1-p
        else:
            nm += 1
    move[p].append(nm)

    st = set([move[0][0]])
    for i in move[0][1::]:
        nst = set()
        for j in st:
            nst.add(j+i)
            nst.add(j-i)
        st = nst.copy()
    if not x in st:
        print("No")
        exit()

    st = set([0])
    for i in move[1]:
        nst = set()
        for j in st:
            nst.add(j+i)
            nst.add(j-i)
        st = nst.copy()
    if not y in st:
        print("No")
        exit()

    print("Yes")

    return None

if __name__ == '__main__':
    main()
