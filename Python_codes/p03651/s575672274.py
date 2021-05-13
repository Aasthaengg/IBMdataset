import sys, math
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
    N, K = mi()
    A = list(mi())

    # Aの最大公約数
    g = A[0]
    for i in range(N):
        g = math.gcd(A[i], g)

    # Aのmax
    m = max(A)
    
    if K%g==0 and m >= K:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')






if __name__ == '__main__':
    main()