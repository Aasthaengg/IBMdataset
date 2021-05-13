import sys, math
from functools import lru_cache
import numpy as np
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


def main():
    S = input()
    N = len(S)
    for i in range(N-1):
        for j in range(i, N):
            if S[:i]+S[j:] == 'keyence':
                print('YES')
                return
    print('NO')


if __name__ == '__main__':
    main()
