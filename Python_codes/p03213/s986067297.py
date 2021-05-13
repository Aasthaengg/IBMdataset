import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def factorization(n):
    factors = []

    if n < 2:
        return n

    while n % 2 == 0:
        factors.append(2)
        n //= 2

    for i in range(3, int(n ** 0.5) + 5, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    if n != 1:
        factors.append(n)

    return factors


def main():
    from collections import Counter

    n = int(input())
    counter = Counter()

    for i in range(2, n + 1):
        factors = factorization(i)
        counter.update(factors)

    x1 = len([c for c in counter.values() if c >= 4])
    y1 = len([c for c in counter.values() if c >= 2])
    x2 = len([c for c in counter.values() if c >= 14])
    y2 = len([c for c in counter.values() if c >= 4])
    x3 = len([c for c in counter.values() if c >= 24])
    y3 = len([c for c in counter.values() if c >= 2])
    x4 = len([c for c in counter.values() if c >= 74])

    ans = 0
    ans += (x1 * (x1 - 1) // 2) * (y1 - 2)
    ans += x2 * (y2 - 1)
    ans += x3 * (y3 - 1)
    ans += x4

    print(ans)


if __name__ == '__main__':
    main()
