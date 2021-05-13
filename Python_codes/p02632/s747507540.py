import sys
input = sys.stdin.readline

mod = 10**9 + 7
K = int(input())
S = input().rstrip()

N = K + len(S)
fact = [1] * (N+1)
fact_inv = [1] * (N+1)
for i in range(1, N+1):
    fact[i] = i * fact[i-1] % mod
fact_inv[N] = pow(fact[N], mod-2, mod)
for i in range(1, N+1)[::-1]:
    fact_inv[i-1] = i * fact_inv[i] % mod
comb = lambda n, k: fact[n] * fact_inv[k] * fact_inv[n-k] % mod

ans = 0
for i in range(K+1):
    ans = (ans + comb(K - i + len(S) - 1, len(S) - 1) * pow(25, K - i, mod) * pow(26, i, mod)) % mod
print(ans)