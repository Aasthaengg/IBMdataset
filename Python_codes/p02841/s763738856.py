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
    M1, D1 = map(int, input().split())
    M2, D2 = map(int, input().split())

    if M1!=M2:
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    main()