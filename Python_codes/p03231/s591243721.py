import sys, math
from functools import lru_cache
from collections import defaultdict
from decimal import Decimal
sys.setrecursionlimit(10**9)
MOD = 10**9+7

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def i2(n):
    tmp = [list(mi()) for i in range(n)]
    return [list(i) for i in zip(*tmp)]

def main():
    N, M = mi()
    S, T = [list(input()), list(input())]

    g = math.gcd(N, M)
    l = N*M//g

    for i in range(g):
        if not (S[N//g*i] == T[M//g*i]):
            print(-1)
            return

    print(l)


if __name__ == '__main__':
    main()
