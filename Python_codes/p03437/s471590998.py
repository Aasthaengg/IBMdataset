import sys, math, re
from functools import lru_cache
from collections import defaultdict
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
    X, Y = mi()
    if X%Y == 0:
        print(-1)
    else:
        print(X)

if __name__ == '__main__':
    main()