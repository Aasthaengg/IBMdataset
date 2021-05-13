# https://atcoder.jp/contests/abc171/tasks/abc171_f

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


    def __call__(self, n, r):  # self.C と同じ
        if not 0 <= r <= n: return 0
        return self.fac[n] * self.facinv[r] % self.mod * self.facinv[n-r] % self.mod

    def C(self, n, r):
        if not 0 <= r <= n: return 0                    # 範囲外という事はすなわち、そのような場合の数は無いはずなので、0を出力すればよい。（これが無いとREになる）
        return self.fac[n] * self.facinv[r] % self.mod * self.facinv[n-r] % self.mod


K = int(input())

S = input()

l = len(S)

MOD = 10**9+7

comb = Combination(K + l + 2)

res = 0

for n in range(K+1):
    res += (comb.C(n + l - 1, l - 1) * pow(25, n, MOD) * pow(26, K-n,MOD))%MOD


print(res%MOD)

