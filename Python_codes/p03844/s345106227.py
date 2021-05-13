# import numpy as np
# import math
# import copy
# from collections import deque
import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10000)


def main():
    A,op,B = input().split()

    A = int(A)
    B = int(B)

    if op == '+':
        res = A + B
    else:
        res = A - B

    print(res)



main()
