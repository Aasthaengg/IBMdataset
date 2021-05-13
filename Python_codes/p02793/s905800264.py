from functools import reduce
MOD = 10**9+7
n = int(input())
A = list(map(int, input().split()))


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return a*(b//gcd(a, b))


x = reduce(lcm, A) % MOD
print(sum(x*pow(a, MOD-2, MOD) for a in A) % MOD)