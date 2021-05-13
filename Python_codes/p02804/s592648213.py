import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def combmod(n, r):
    res = 1

    for i in range(r):
        res *= (n - i)
        res %= MOD
        res *= pow((r - i), MOD - 2, MOD)

    nextdiv = n
    nextmul = n - r

    while res > 0:
        yield res
        res *= pow(nextdiv, MOD - 2, MOD)
        res %= MOD
        res *= nextmul
        res %= MOD
        nextdiv -= 1
        nextmul -= 1


def main():
    n0, k0 = list(map(int, readline().split()))
    a0 = list(map(int, readline().split()))

    a0.sort()

    ans = 0

    for i, com in enumerate(combmod(n0 - 1, k0 - 1)):
        ans += a0[-i - 1] * com
        ans %= MOD
        ans -= a0[i] * com
        ans %= MOD

    print(ans)


if __name__ == '__main__':
    main()
