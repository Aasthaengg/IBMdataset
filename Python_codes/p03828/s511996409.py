import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from collections import Counter

    n = int(readline())
    factors = Counter()

    for i in range(2, n + 1):
        x = i
        for j in range(2, int(i ** 0.5) + 5):
            while x % j == 0:
                factors[j] += 1
                x //= j
        if x != 1:
            factors[x] += 1

    ans = 1

    for key, val in factors.items():
        ans *= (val + 1)
        ans %= MOD

    print(ans)


if __name__ == '__main__':
    main()
