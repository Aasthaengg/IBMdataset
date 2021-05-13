import sys
import math
import itertools


def input():
    return sys.stdin.readline().rstrip()


def main():
    N, M = map(int, input().split())
    L = 1
    R = 10 ** 5 + 1

    for i in range(M):
        l, r = map(int, input().split())
        L = max(l, L)
        R = min(r, R)

    print(max(R-L+1,0))


if __name__ == "__main__":
    main()
