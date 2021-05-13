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
    n = input()
    ln = len(n)
    ma = sum(map(int,n))
    ma2 = int(n[0])-1+9*(ln-1)
    if ma < ma2:
        print(ma2)
    else:
        print(ma)


    return None

if __name__ == '__main__':
    main()
