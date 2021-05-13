import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def comb_mod(n, r):
    res = 1
    r = min(n - r, r)

    for i in range(r):
        res *= (n - i)
        res %= MOD
        res *= pow((r - i), MOD - 2, MOD)

    return res


def main():
    k = int(readline())
    s = input()
    l = len(s)
    x = k + l

    comb = 1
    ans = 0
    for i in range(k + 1):
        ans += pow(26, k - i, MOD) * pow(25, i, MOD) * comb
        ans %= MOD
        comb *= (l + i)
        comb %= MOD
        comb *= pow(i + 1, MOD - 2, MOD)
        comb %= MOD

    print(ans)


if __name__ == '__main__':
    main()
