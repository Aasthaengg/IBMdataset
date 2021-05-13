k = int(input())
s = input()
mod = 10 ** 9 + 7

MAX = 2 * 10 ** 6

fact = [1] * (MAX + 1)
for i in range(1, MAX + 1):
    fact[i] = (fact[i-1] * i) % mod

inv = [1] * (MAX + 1)
for i in range(2, MAX + 1):
    inv[i] = inv[mod % i] * (mod - mod // i) % mod

fact_inv = [1] * (MAX + 1)
for i in range(1, MAX + 1):
    fact_inv[i] = fact_inv[i-1] * inv[i] % mod


def comb(n, k):
    if n < k:
        return 0
    return fact[n] * fact_inv[n-k] * fact_inv[k] % mod


ln = len(s)

ans = 0
pow25 = 1
pow26 = pow(26, k, mod)
inv26 = pow(26, mod - 2, mod)
for i in range(ln, k + ln + 1):
    ans += pow25 * pow26 % mod * comb(i - 1, ln - 1) % mod
    ans %= mod
    pow25 *= 25
    pow25 %= mod
    pow26 *= inv26
    pow26 %= mod

print(ans)
