import sys
input = sys.stdin.readline
import math


def read():
    N = int(input().strip())
    return N,


def solve(N):
    # (m+1)p=N, 0 < p < mを満たすmを列挙する
    ans = 0
    p = 1
    while p * p <= N:
        if N % p == 0:
            m = N // p - 1
            if p < m:
                ans += m
            else:
                break
        p += 1
    return ans


if __name__ == '__main__':
    inputs = read()
    print(solve(*inputs))
