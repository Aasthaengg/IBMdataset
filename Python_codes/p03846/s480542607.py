# import numpy as np
# import math
# import copy
# from collections import deque
import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10000)


def main():
    N = int(input())
    A = list(map(int,input().split()))

    mod = 10 ** 9 + 7

    count = [0 for i in range(N)]

    for i in range(N):
        count[A[i]] += 1

    M = N % 2

    res = 1

    if M == 1:
        if count[0] != 1:
            print(0)
            sys.exit()
        test = 0
        for i in range(1,N):
            if count[i] == test:
                res *= max(test,1)
                res %= mod
            else:
                res = 0
                break
            if test == 0:
                test = 2
            else:
                test = 0
    else:
        if count[0] != 0:
            print(0)
            sys.exit()
        test = 2
        for i in range(1,N):
            if count[i] == test:
                res *= max(test,1)
                res %= mod
            else:
                res = 0
                break
            if test == 0:
                test = 2
            else:
                test = 0

    print(res)



main()
