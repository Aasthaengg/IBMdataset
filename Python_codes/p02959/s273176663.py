import sys

sys.setrecursionlimit(10 ** 7)
# import bisect
# import numpy as np
# from collections import deque
from collections import deque
# map(int, sys.stdin.read().split())
import itertools
import heapq


def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    res = 0
    mons = 0
    for i in range(N):
        if B[i] + res > A[i]:
            mons += A[i]
            res = min(B[i], B[i] + res - A[i])
        else:
            mons += B[i] + res
            res = 0
    ##saigo
    if res > A[N]:
        mons += A[N]
    else:
        mons += res
    print(mons)

if __name__ == "__main__":
    main()
