import sys
import math

mod = 998244353

def modinv(a, mod=10**9+7):
    return pow(a, mod-2, mod)

N, M, K = map(int, sys.stdin.readline().strip().split())

fact = [1 for i in range(N+1)]
for i in range(1, N):
    fact[i+1] = (fact[i] * (i+1)) % mod

# math.factroialでは速度が足りない
def nCr(n, r, mod=10**9+7):
    if n < 0 or r < 0 or n < r:
        return 0

    if n == 0 or r == 0:
        return 1

    """
    a = math.factorial(n) % mod
    b = math.factorial(r) % mod
    c = math.factorial(n - r) % mod
    """
    a = fact[n]
    b = fact[r]
    c = fact[n-r]

    inv = modinv(b*c, mod)
    ans = a * inv

    return ans % mod


ans = 0
for i in range(K+1):
    ans += nCr(N - 1, i, mod) * (M * pow(M-1, N-1-i, mod))
    # print(ans)
    ans %= mod

print(ans)