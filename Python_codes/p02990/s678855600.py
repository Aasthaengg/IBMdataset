N, K = map(int, input().split())
MOD = 10 ** 9 + 7

MAX = 4000
fact = [0] * MAX
invfact = [0] * MAX
fact[0] = 1
for i in range(1, MAX):
    fact[i] = fact[i - 1] * i % MOD
invfact[MAX - 1] = pow(fact[MAX - 1], MOD-2, MOD)
for i in range(MAX - 2, -1, -1):
    invfact[i] = invfact[i+1] * (i+1) % MOD

def nCk(n, k):
    if k < 0 or n < k: return 0
    return (fact[n] * invfact[k] % MOD) * invfact[n-k] % MOD

ans = 0
red = N - K
for i in range(1,1+K):
    ans = nCk(red+1, i) * nCk(K-1, i-1)
    ans %= MOD
    print(ans)

