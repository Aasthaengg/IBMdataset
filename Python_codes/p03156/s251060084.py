import sys, math
from functools import lru_cache
from collections import deque
sys.setrecursionlimit(500000)
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
    A, B = mi()
    P = list(mi())
    diff_a = sum(1 for p in P if p <= A)
    diff_b = sum(1 for p in P if A < p <= B)
    diff_c = sum(1 for p in P if p > B)
    print(min(diff_a, diff_b, diff_c))


if __name__ == '__main__':
    main()