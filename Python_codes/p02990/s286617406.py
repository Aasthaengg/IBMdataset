import math
n, k = map(int, input().split())
mod = 10**9 + 7

modinv_table = [-1] * (k+1)
modinv_table[1] = 1
for i in range(2, k+1):
    modinv_table[i] = (-modinv_table[mod % i] * (mod // i)) % mod

def binomial_coefficients(n, k):
    ans = 1
    for i in range(k):
        ans *= n-i
        ans *= modinv_table[i + 1]
        ans %= mod
    return ans

for i in range(1,k+1):
    print(int(binomial_coefficients(n-k+1, i)*binomial_coefficients(k-i+i-1, i-1)%mod))