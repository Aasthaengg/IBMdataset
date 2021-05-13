import sys
import math

input = sys.stdin.readline


def prime_factorization(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def main():
    N = int(input())

    ef = [0] * (N + 1)
    ans = 0
    for i in range(2, N + 1):
        x = prime_factorization(i)
        for xx in x:
            ef[xx] += 1

    a, b, c, d, e = 0, 0, 0, 0, 0
    for ee in ef:
        if ee >= 74:
            a += 1
            b += 1
            c += 1
            d += 1
            e += 1
        elif ee >= 24:
            a += 1
            b += 1
            c += 1
            d += 1
        elif ee >= 14:
            a += 1
            b += 1
            c += 1
        elif ee >= 4:
            a += 1
            b += 1
        elif ee >= 2:
            a += 1

    ans += e
    ans += d * (a - 1)
    ans += c * (b - 1)
    ans += b * (b - 1) * (a - 2) // 2

    print(ans)


if __name__ == '__main__':
    main()
