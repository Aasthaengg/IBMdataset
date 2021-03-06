MAX = 10**6 * 3
MOD = 10**9+7
fac = [0] * MAX
finv = [0] * MAX
inv = [0] * MAX
#前処理 逆元テーブルを作る
def COMinit():
    fac[0] = 1
    fac[1] = 1
    finv[0] = 1
    finv[1] = 1
    inv[1] = 1
    for i in range(2, MAX):
        fac[i] = fac[i-1] * i % MOD
        inv[i] = MOD - inv[MOD%i] * (MOD//i)%MOD
        finv[i] = finv[i-1] * inv[i] % MOD
#実行
def COM(n, k):
    if n  < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n-k] % MOD) % MOD
k = int(input())
s = input()
n = len(s)
COMinit()
ans = 0
for i in range(k+1):
    pls = pow(25, i, MOD)
    pls *= pow(26,k-i, MOD)
    pls %= MOD
    pls *= COM(i+n-1, i)
    ans += pls
    ans %= MOD
print(ans%MOD)