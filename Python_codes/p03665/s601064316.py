import sys
input = sys.stdin.readline
from collections import Counter 


def read():
    N, P = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))
    return N, P, A


def binom_64bit(n):
    c = [1 for i in range(n+1)]
    for k in range(1, n):
        c[k] = c[k-1] * (n-k+1) // k
    return c


def solve(N, P, A):
    B = Counter([a % 2 for a in A])
    C0 = binom_64bit(B[0])
    C1 = binom_64bit(B[1])
    ans = 0
    if P == 1:
        for i in range(0, B[0]+1):
            for j in range(1, B[1]+1, 2):
                ans += C0[i] * C1[j]
    else:
        for i in range(0, B[0]+1):
            for j in range(0, B[1]+1, 2):
                ans += C0[i] * C1[j]
    return ans


if __name__ == '__main__':
    inputs = read()
    print("%s" % solve(*inputs))
