import sys

mod = 10 ** 9 + 7
sys.setrecursionlimit(mod)

def modpow(a, p):
    if p == 0:
        return 1
    if p % 2 == 0:
        half = modpow(a, p // 2)
        return half * half % mod
    else:
        return a * modpow(a, p - 1) % mod

def combinations(a, b):
    if 2 * b > a:
        return combinations(a, a - b)
    mul = 1
    div = 1
    for i in range(b):
        mul *= (a - i)
        div *= (i + 1)
        mul %= mod
        div %= mod
    return mul * modpow(div, mod - 2) % mod

N, M = map(int, input().split())
i = 2
ans = 1
while i * i <= M:
    if M % i == 0:
        c = 0
        while M % i == 0:
            c += 1
            M /= i
        ans *= combinations(N + c - 1, N - 1)
        ans %= mod
    i += 1

if M != 1:
    ans *= combinations(N + 1 - 1, N - 1)
    ans %= mod

print(ans)