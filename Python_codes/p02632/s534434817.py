MOD = 10**9 + 7
MAX = 5*10**6 + 1

fact = [0 for _ in range(MAX)]
factinv = [0 for _ in range(MAX)]

fact[0] = 1
for k in range(1, MAX):
    fact[k] = fact[k - 1]*k
    fact[k] %= MOD

factinv[MAX - 1] = pow(fact[MAX - 1], MOD - 2, MOD)
for k in range(MAX - 1, 0, -1):
    factinv[k - 1] = factinv[k]*k
    factinv[k - 1] %= MOD

def nCk(n, k):
    return fact[n]*factinv[k]*factinv[n - k] % MOD

def nPk(n, k):
    return fact[n]*factinv[n - k] % MOD

K = int(input())
S = input()
N = len(S)

ans = 0
for k in range(K + 1):
    ans += nCk(N + K - k - 1, N - 1)*pow(26, k, MOD)*pow(25, K - k, MOD) % MOD
    ans %= MOD

print(ans)