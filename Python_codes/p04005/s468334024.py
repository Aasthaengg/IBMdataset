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
    X = list(mi())

    if all(x%2==1 for x in X):
        print(min(X[0]*X[1], X[1]*X[2], X[2]*X[0]))
    else:
        print(0)

if __name__ == '__main__':
    main()
