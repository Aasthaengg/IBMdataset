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
    s = input()
    if s.count('R') > N/2:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
