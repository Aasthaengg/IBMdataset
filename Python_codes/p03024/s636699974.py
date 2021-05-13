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
alp = "abcdefghijklmnopqrstuvwxyz"

def main():
    s = input()
    n = len(s)
    nm = 0
    for i in s:
        if i == "o":
            nm += 1

    if nm >= 8-(15-n):
        print("YES")
    else:
        print("NO")

    return None

if __name__ == '__main__':
    main()
