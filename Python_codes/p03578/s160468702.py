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

# nまでの自然数が素数かどうかを表すリストを返す
def makePrimeChecker(n):
    isPrime = [True] * (n + 1)
    isPrime[0] = False
    isPrime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if isPrime[i]:
            for j in range(i * i, n + 1, i):
                isPrime[j] = False
    return isPrime


def main():
    N = ii()
    D = list(mi())
    M = ii()
    T = list(mi())

    d = defaultdict(int)
    for i in range(N):
        d[D[i]] += 1

    t = defaultdict(int)
    for i in range(M):
        d[T[i]] -= 1

    for v in d.values():
        if v < 0:
            print('NO')
            return
    
    print('YES')

if __name__ == '__main__':
    main()
