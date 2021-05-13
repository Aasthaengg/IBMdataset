import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
mod = 10**9 + 7

fact = [1] * (N+1)
fact_inv = [1] * (N+1)
for i in range(1, N+1):
    fact[i] = i * fact[i-1] % mod
fact_inv[N] = pow(fact[N], mod-2, mod)
for i in range(1, N+1)[::-1]:
    fact_inv[i-1] = i * fact_inv[i] % mod
combination = lambda n, k: fact[n] * fact_inv[k] * fact_inv[n-k] % mod

A.sort()
ans = 0
for i in range(N):
    if i >= K - 1:
        ans += A[i] * combination(i, K - 1)
    if N - i - 1 >= K - 1:
        ans -= A[i] * combination(N - i - 1, K - 1)
    ans %= mod
print(ans)