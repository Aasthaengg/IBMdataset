import sys, math
from functools import lru_cache
import numpy as np
import heapq
from collections import defaultdict
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


def lcm(a, b):
    return a*b//math.gcd(a, b)


def main():
    N = ii()
    A = list(mi())
    cnt = 0
    for i in range(N):
        if A[i]%2==1:
            cnt += 1
    if cnt%2 == 1:
        print('NO')
    else:
        print('YES')

if __name__ == '__main__':
    main()
