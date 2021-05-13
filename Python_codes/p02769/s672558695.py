MAX = 1000005
MOD = 10**9+7
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


N, K = map(int, input().split())
ans = 0
for i in range(min(K, N)+1):  # 空にできるのはK部屋または、N-1部屋までのみ。
    ans += COM(N, i) * COM(N-1, i)
    ans %= MOD
print(ans)
