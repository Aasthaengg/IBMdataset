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
    S = input()

    N = len(S) + 1
    a = [0] * N 
    for i in range(N-1):
        if S[i] == "<":
            a[i+1] = max(a[i+1], a[i]+1)
    for i in reversed(range(N-1)):
        if S[i] == ">":
            a[i] = max(a[i], a[i+1]+1)
    
    print(sum(a))


if __name__ == '__main__':
    main()