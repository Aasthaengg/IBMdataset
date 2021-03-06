
class Combination:
    def __init__(self, n_max, mod=10 ** 9 + 7):
        # O(n_max + log(mod))
        self.mod = mod
        f = 1
        self.fac = fac = [f]
        for i in range(1, n_max + 1):
            f = f * i % mod
            fac.append(f)
        f = pow(f, mod - 2, mod)
        self.facinv = facinv = [f]
        for i in range(n_max, 0, -1):
            f = f * i % mod
            facinv.append(f)
        facinv.reverse()

    # "n 要素" は区別できる n 要素
    # "k グループ" はちょうど k グループ

    def __call__(self, n, r):  # self.C と同じ
        return self.fac[n] * self.facinv[r] % self.mod * self.facinv[n - r] % self.mod

    def nCr(self, n, r):
        if not 0 <= r <= n:
            return 0
        return self.fac[n] * self.facinv[r] % self.mod * self.facinv[n - r] % self.mod

def resolve():
    # 各集合Sのmax(S) - min(S)の合計を求める
    # 各A[i]が最大値になる回数、最小値になる回数を求め、それを計算する
    MOD = 10**9+7
    N, K = map(int, input().split())
    A = sorted(map(int, input().split()))

    Comb = Combination(N)
    ans = 0
    for i in range(N):
        # 最大値になる組み合わせは、A[j]: 0 < j < iからK - 1個を選ぶ組み合わせ
        ans += Comb.nCr(i, K-1) * A[i] % MOD
        ans %= MOD
        # 最小値になる組み合わせは、A[j]: i < j < nからK-1個を選ぶ組み合わせ
        ans -= Comb.nCr(N-i-1, K - 1) * A[i]% MOD
        ans %= MOD
    print(ans)


if __name__ == "__main__":
    resolve()
