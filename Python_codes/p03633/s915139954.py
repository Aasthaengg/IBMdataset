import sys
from fractions import gcd

input = sys.stdin.readline


def lcm(a, b):
    return (a * b) // gcd(a, b)


def main():
    N = int(input())
    T = [0] * N
    for i in range(N):
        T[i] = int(input())

    ans = T[0]
    for i in range(1, N):
        ans = lcm(ans, T[i])

    print(ans)


if __name__ == "__main__":
    main()
