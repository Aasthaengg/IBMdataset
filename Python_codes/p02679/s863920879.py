import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    import fractions
    import math
    from collections import Counter
    n = int(readline())
    counter = Counter()
    a0, b0 = 0, 0
    lonely = 0

    for i in range(n):
        a, b = map(int, readline().split())
        if a == 0 and b == 0:
            lonely += 1
        elif a == 0:
            a0 += 1
        elif b == 0:
            b0 += 1
        else:
            fr = fractions.Fraction(a, b)
            counter[(fr.numerator, fr.denominator)] += 1

    ans = 1  # 最後に
    keys = list(counter.keys())
    for key in keys:
        nm1, dn1 = key[0], key[1]
        cnt1 = counter[(nm1, dn1)]
        nm2, dn2 = -(nm1 // abs(nm1)) * dn1, abs(nm1)
        cnt2 = counter[(nm2, dn2)]
        ans = ans * ((pow(2, cnt1, MOD) - 1) + (pow(2, cnt2, MOD) - 1) + 1)
        ans %= MOD
        counter[(nm1, dn1)] = 0
        counter[(nm2, dn2)] = 0

    ans *= ((pow(2, a0, MOD) - 1) + (pow(2, b0, MOD) - 1) + 1)
    ans %= MOD
    ans += lonely
    ans -= 1
    ans %= MOD

    print(ans)


if __name__ == '__main__':
    main()
