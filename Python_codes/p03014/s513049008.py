import math
#import numpy as np
import queue
from collections import deque,defaultdict
import heapq
from sys import stdin,setrecursionlimit
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse import csr_matrix
ipt = stdin.readline
setrecursionlimit(10**7)

def main():
    h,w = map(int,ipt().split())
    s = [""]*h+["#"*(w+1)]
    for i in range(h):
        s[i] = input()+"#"
    l = [[0]*(w+1) for _ in [0]*(h+1)]
    r = [[0]*(w+1) for _ in [0]*(h+1)]
    u = [[0]*(w+1) for _ in [0]*(h+1)]
    d = [[0]*(w+1) for _ in [0]*(h+1)]
    sm = [[-3]*(w+1) for _ in [0]*(h+1)]
    for i in range(h):
        si = sm[i]
        li = l[i]
        ui = u[i]
        for j in range(w):
            if s[i][j] == "#":
                continue
            else:
                li[j] = l[i-1][j]+1
                ui[j] = ui[j-1]+1
                si[j] += li[j]+ui[j]
    ma = 0
    for i in range(h):
        ri = r[h-i-1]
        si = sm[h-i-1]
        di = d[h-i-1]
        for j in range(w):
            if s[h-i-1][w-j-1] == "#":
                continue
            else:
                ri[w-j-1] = r[h-i][w-j-1]+1
                di[w-j-1] = di[w-j]+1
                si[w-j-1] += ri[w-j-1]+di[w-j-1]
                if ma < si[w-j-1]:
                    ma = si[w-j-1]
    print(ma)


    return

if __name__ == '__main__':
    main()
