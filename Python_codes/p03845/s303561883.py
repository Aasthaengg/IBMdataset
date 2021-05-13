import sys
sys.setrecursionlimit(4100000)
import math
import itertools
INF = float('inf')
from heapq import heapify, heappop, heappush
import collections
import bisect

def main():
    n = int(input())
    T = list(map(int, input().split()))
    m = int(input())
    P =[]
    X =[]
    for i in range(m):
        p,x = map(int, input().split())
        P.append(p)
        X.append(x)

    total = sum(T)
    for i in range(m):
        print(total - (T[P[i]-1] - X[i]))


if __name__ == '__main__':
    main()
