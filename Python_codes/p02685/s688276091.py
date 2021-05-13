class Combination:                                      # 計算量は O(n_max + log(mod))
    def __init__(self, n_max, mod=10**9+7):
        self.mod = mod
        f = 1
        self.fac = fac = [f]
        for i in range(1, n_max+1):                     # 階乗(= n_max !)の逆元を生成
            f = f * i % mod                             # 動的計画法による階乗の高速計算
            fac.append(f)                               # fac は階乗のリスト
        f = pow(f, mod-2, mod)                          # 階乗から階乗の逆元を計算。フェルマーの小定理より、　a^-1 = a^(p-2) (mod p) if p = prime number and p and a are coprime
                                                        # python の pow 関数は自動的に mod の下での高速累乗を行ってくれる
        self.facinv = facinv = [f]
        for i in range(n_max, 0, -1):                   # 上記の階乗の逆元から階乗の逆元のリストを生成（＝ facinv ）
            f = f * i % mod
            facinv.append(f)
        facinv.reverse()

    def H(self, n, r):                                  # (箱区別:〇　ボール区別:×　空箱:〇)　重複組み合わせ nHm
        if (n == 0 and r > 0) or r < 0: return 0
        return self.fac[n+r-1] * self.facinv[r] % self.mod * self.facinv[n-1] % self.mod

N, M, K = map(int, input().split())
MOD=998244353
C = Combination(N,MOD)
res = 0
p=pow(M-1,N-K-1,MOD)
for k in range(K,-1,-1):
    res += C.H(N - k,k) * M * p
    p *= (M-1)
    p %= MOD
    res %= MOD
print(res)