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
    H, W, N = [ii(), ii(), ii()]
    print(math.ceil(N/max(H, W)))


if __name__ == '__main__':
    main()