from functools import reduce
from fractions import gcd
import math
import bisect
import itertools
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
INF = float("inf")


def main():
    N, K = map(int, input().split())
    
    res = K
    for i in range(N-1):
        res *= K - 1
    
    print(res)
    

if __name__ == '__main__':
    main()