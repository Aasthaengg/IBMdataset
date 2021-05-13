import sys
from fractions import gcd

input = sys.stdin.readline


def lcm(a, b):
    return (a * b) // gcd(a, b)


def main():
    N, M = map(int, input().split())
    S = input().rstrip()
    T = input().rstrip()

    L = lcm(N, M)
    n = L // N
    m = L // M

    ans = L
    i = 0
    while i < L // (n * m):
        if S[m * i] != T[n * i]:
            ans = -1
            break
        i += 1

    print(ans)


if __name__ == "__main__":
    main()
