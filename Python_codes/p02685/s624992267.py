# 二項係数を"やるだけ"にしてくれるライブラリ
from collections import Counter
MAX = 1000005
MOD = 998244353
factrial = [0]*MAX
inverse = [0]*MAX
factrial_inverse = [0]*MAX


# テーブルを作る前処理
def COMinit():
    global factrial, inverse, factrial_inverse
    factrial[0] = 1
    factrial[1] = 1
    inverse[1] = 1
    factrial_inverse[0] = 1
    factrial_inverse[1] = 1
    for i in range(2, MAX):
        factrial[i] = factrial[i-1] * i % MOD
        inverse[i] = MOD - inverse[MOD % i] * (MOD//i) % MOD
        factrial_inverse[i] = factrial_inverse[i-1] * inverse[i] % MOD


# 二項係数計算
def COM(n, k):
    global factrial, inverse, factrial_inverse
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return factrial[n] * (factrial_inverse[k] * factrial_inverse[n-k] % MOD) % MOD


# 前処理完了
COMinit()

N, M, K = map(int, input().split())  # N個のブロック, M色のパターン, 隣合う組で色が同じなのはK組以下
# 同じ色の組が0~Kを考える
ans = 0
for i in range(K+1):
    # i: 消滅させるブロック
    ans += M * pow(M-1, N-1-i, MOD) * COM(N-1, i)
    ans %= MOD

print(ans%MOD)