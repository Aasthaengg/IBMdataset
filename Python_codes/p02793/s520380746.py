import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from collections import Counter
    n = int(input())
    a = list(map(int, readline().split()))

    def factorization(n):
        factors = []

        while n % 2 == 0:
            factors.append(2)
            n //= 2

        for i in range(3, int(n ** 0.5) + 5, 2):
            while n % i == 0:
                factors.append(i)
                n //= i
        if n != 1:
            factors.append(n)

        return Counter(factors)

    a_fac = [0] * n

    for i, num in enumerate(a):
        a_fac[i] = factorization(num)

    lcm = {1: 1}

    for fac in a_fac:
        for key, value in fac.items():
            lcm[key] = max(lcm.get(key, 0), value)

    ans = 0

    lcmmod = 1

    for key, value in lcm.items():
        lcmmod *= pow(key, value, MOD)
        lcmmod %= MOD

    for ele in a:
        ainv = pow(ele, MOD - 2, MOD)
        ans += ((lcmmod*ainv) % MOD)
        ans %= MOD

    print(ans)


if __name__ == '__main__':
    main()
