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
    c = 0
    d = 0

    for i in range(N-1):
        for j in range(i+1, N):
            if A[i] > A[j]:
                c += 1
    
    for i in range(N):
        for j in range(N):
            if A[i] < A[j]:
                d += 1

    ans = (K*(K-1)//2)%MOD
    ans *= d
    ans %= MOD
    ans += (K*c)%MOD
    ans %= MOD

    print(ans)

if __name__ == '__main__':
    main()