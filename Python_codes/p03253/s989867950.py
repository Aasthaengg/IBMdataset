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

    n, m = list(map(int, readline().split()))

    if m == 1:
        print(1)
        sys.exit()

    factors = Counter(factorization(m))

    ans = 1

    for cnt in factors.values():
        for i in range(1, cnt + 1):
            ans *= (n + cnt - i)
            ans %= MOD
            ans *= pow(i, MOD - 2, MOD)
            ans %= MOD

    print(ans)

if __name__ == '__main__':
    main()
