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
    n = int(ipt())
    s = input()
    ma = 0
    for i in range(n):
        pf = z_algorithm(s[i::])
        if pf > ma:
            ma = pf
    print(ma)

def z_algorithm(s):
    ma = 0
    prefix = [0]*len(s)
    j = 0
    for i in range(1,len(s)):
        if i+prefix[i-j] < j+prefix[j]:
            prefix[i] = prefix[i-j]
        else:
            k = max(0,j+prefix[j]-i)
            while i+k < len(s) and s[k] == s[i+k]:
                k += 1
            prefix[i] = k
            j = i
    for i,pi in enumerate(prefix):
        if i < pi:
            prefix[i] = i
    for pi in prefix:
        if ma < pi:
            ma = pi
    return ma

if __name__ == '__main__':
    main()
