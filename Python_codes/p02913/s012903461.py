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
    prefix[0] = len(s)
    for i,pi in enumerate(prefix):
        if i < pi:
            prefix[i] = i
    for i in prefix:
        if ma < i:
            ma = i
    return ma

def main():
    n = int(ipt())
    s = input()
    ma = 0
    for i in range(n):
        pf = z_algorithm(s[i::])
        if ma < pf:
            ma = pf

    print(ma)

    return None

if __name__ == '__main__':
    main()
