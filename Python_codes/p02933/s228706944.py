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
    a = int(input())
    s = input()[:-1]

    if a>=3200:
        print(s)
    else:
        print("red")


if __name__ == '__main__':
    main()