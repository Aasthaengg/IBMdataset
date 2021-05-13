N, K = map(int, input().split())
A=list(map(int, input().split()))
A.sort()
MOD=10**9+7
s_max = 0
s_min = 0
MAX = 10**5 + 100
def COMinit():
    """
    逆元テーブルをつくる前処理
    計算量はO(n)
    1 <= k <= n <= 1e7程度
    p: 素数
    """
    fac = [0]*MAX
    finv = [0]*MAX
    inv = [0]*MAX

    fac[0], fac[1] = 1, 1
    finv[0], finv[1] = 1, 1
    inv[0], inv[1] = 1, 1
    for i in range(2, MAX):
        fac[i] = fac[i-1] * i % MOD
        inv[i] = MOD - inv[MOD%i] * (MOD // i) % MOD
        finv[i] = finv[i-1] * inv[i] % MOD
    return fac, finv, inv



def comb(n, k):
    """
    nCk mod MODを求める.
    この部分はO(1)
    """
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return int(fac[n] * (finv[k] * finv[n-k] % MOD) % MOD)

fac, finv, inv = COMinit()

for i in range(N):
    s_min += comb(N-i-1, K-1) * A[i]
    s_min %= MOD
for i in range(N-1, -1, -1):
    s_max += comb(i, K-1) * A[i]
    s_max %= MOD
print((s_max - s_min)%MOD)