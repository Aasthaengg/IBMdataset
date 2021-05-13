import sys, math
from functools import lru_cache
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
    m = 10**100
    for i in range(1, N//2+1):
        A = i
        B = N-i
        Da = sum(int(a) for a in str(A))
        Db = sum(int(b) for b in str(B))
        m = min(m, Da+Db)
    print(m)


if __name__ == '__main__':
    main()