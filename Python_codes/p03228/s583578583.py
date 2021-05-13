import sys, math
from functools import lru_cache
import datetime
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
    A, B, K = mi()
    for i in range(K):
        if i%2 == 0:
            if A%2:
                A -= 1
            B += A//2
            A -= A//2
        else:
            if B%2:
                B -= 1
            A += B//2
            B -= B//2

    print(A, B)



if __name__ == '__main__':
    main()