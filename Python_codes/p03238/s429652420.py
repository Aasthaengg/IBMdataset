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
    n = int(input())
    if n == 1:
        print("Hello World")
    else:
        A = int(input())
        B = int(input())
        print(A+B)


if __name__ == '__main__':
    main()