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
    N = ii()
    k = 1
    while k*(k+1)//2 < N:
        k += 1
    if k*(k+1)//2 > N:
        k -= 1

    r = N-(k*(k+1)//2)

    for i in range(k, 0, -1):
        if i > k-r:
            print(i+1)
        else:
            print(i)


if __name__ == '__main__':
    main()
