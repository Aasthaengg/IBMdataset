import sys, math, re
from functools import lru_cache
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
    N, M, K = mi()

    for k in range(N+1):
        for l in range(M+1):
            if k*(M-l)+(N-k)*l == K:
                print('Yes')
                return

    print('No')


if __name__ == "__main__":
    main()