import sys, bisect, math, itertools, string, queue, copy
# import numpy as np
# import scipy
# from scipy.sparse.csgraph import floyd_warshall
from collections import Counter,defaultdict,deque
from itertools import permutations, combinations, combinations_with_replacement
from heapq import heappop, heappush, heapify
from fractions import gcd
# input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7

def main():
    n,d = map(int,input().split())
    ans = 0
    for _ in range(n):
        x,y = map(int,input().split())
        if (x**2 + y**2)**0.5 <= d:
            ans += 1
    print(ans)
    
if __name__ == "__main__":
    main()