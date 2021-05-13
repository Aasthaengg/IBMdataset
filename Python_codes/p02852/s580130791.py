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
    N, M = map(int, input().split())
    S = input()[:-1][::-1]
    # print(S)

    res = []
    n = 0
    while n < N:
        miss = True
        for m in reversed(range(1,M+1)):
            if n+m < N+1 and S[n+m] == "0":
                n += m
                res.append(str(m))
                miss = False
                break
        if miss:
            print(-1)
            return
        
    print(" ".join(reversed(res)))

    


if __name__ == '__main__':
    main()