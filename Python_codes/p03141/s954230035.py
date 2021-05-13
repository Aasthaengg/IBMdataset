import sys, math
from functools import lru_cache
import heapq
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
    N = ii()
    A, B = i2(N)
    ans = 0

    C = [(a + b, i) for a, b, i in zip(A, B, range(N))]
    C.sort(reverse=True)

    for i in range(N):
        k = C[i][1]
        if i%2==0:
            ans += A[k]
        else:
            ans -= B[k]

    print(ans)


if __name__ == '__main__':
    main()
