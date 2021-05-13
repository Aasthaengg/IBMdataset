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
    N = int(input())
    x = [0]*N
    y = [0]*N
    h = [0]*N
    for i in range(N):
        x[i], y[i], h[i] = map(int, input().split())
    
    for Cx in range(101):
        for Cy in range(101):
            H = INF
            for i in range(N):
                if h[i] > 0:
                    H = h[i] + abs(x[i]-Cx) + abs(y[i]-Cy)

            flg = True
            for i in range(N):
                if max(H - abs(x[i]-Cx) - abs(y[i]-Cy), 0) != h[i]:
                    flg = False
                    break
            if flg:
                print(" ".join([str(Cx), str(Cy), str(H)]))
                return


if __name__ == '__main__':
    main()
