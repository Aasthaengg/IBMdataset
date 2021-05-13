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

    cnt = 0
    ans = 0
    for i in range(len(S)):
        if S[i] == "W":
            ans += i - cnt
            cnt += 1
    
    print(ans)


if __name__ == '__main__':
    main()