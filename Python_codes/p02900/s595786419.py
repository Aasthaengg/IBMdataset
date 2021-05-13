import sys
import math
input = lambda: sys.stdin.readline().rstrip()


def factorize(n):
    b = 2
    fct = set()
    while b * b <= n:
        while n % b == 0:
            n //= b
            fct |= set([b])
        b = b + 1
    if n > 1:
        fct |= set([n])
    return fct


def solve():
    A, B = map(int, input().split())
    ap = factorize(A)
    bp = factorize(B)
    ans = 1 + len(ap & bp)
    print(ans)


if __name__ == '__main__':
    solve()
