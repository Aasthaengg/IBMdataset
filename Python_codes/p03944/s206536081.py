import sys
sys.setrecursionlimit(4100000)
import math
import itertools
INF = float('inf')
from heapq import heapify, heappop, heappush
import collections
import bisect

def main():
    w,h,n = map(int, input().split())
    X = []
    Y = []
    A = []
    for i in range(n):
        x,y,a = map(int, input().split())
        X.append(x)
        Y.append(y)
        A.append(a)

    plots = [[0,0], [w,0], [w,h], [0,h]]
    for i in range(n):
        if A[i] == 1:
            plots[0][0] = max(plots[0][0], X[i])
            plots[3][0] = max(plots[3][0], X[i])
        elif A[i] == 2:
            plots[1][0] = min(plots[1][0], X[i])
            plots[2][0] = min(plots[2][0], X[i])
        elif A[i] == 3:
            plots[0][1] = max(plots[0][1], Y[i])
            plots[1][1] = max(plots[1][1], Y[i])
        else:
            plots[2][1] = min(plots[2][1], Y[i])
            plots[3][1] = min(plots[3][1], Y[i])
    width = plots[1][0] - plots[0][0]
    height = plots[2][1] - plots[1][1]
    if width <= 0 or height <= 0:
        print(0)
        return
    print(width * height)


if __name__ == '__main__':
    main()
