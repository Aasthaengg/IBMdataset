class Combination:
    def __init__(self, n_max, MOD=10 ** 9 + 7):
        """
        前処理 = O(n_max + log(MOD))
        :param self.fac[n]: n!
        :param self.facinv[n]: 1/n!
        """
        self.mod = MOD
        f = 1
        self.fac = fac = [f]
        for i in range(1, n_max+1):
            f = f * i % MOD
            fac.append(f)
        f = pow(f, MOD - 2, MOD)
        self.facinv = facinv = [f]
        for i in range(n_max, 0, -1):
            f = f * i % MOD
            facinv.append(f)
        facinv.reverse()

    def __call__(self, n, r):  # self.C と同じ
        if not 0 <= r <= n: return 0
        return self.fac[n] * self.facinv[r] % self.mod * self.facinv[n-r] % self.mod


N, P = map(int, input().split())
A = []
for a in map(int, input().split()):
    A.append(a%2)
cnt1 = A.count(1)
cnt0 = N - cnt1
C = Combination(cnt1)
if P==1:
    res = sum(C(cnt1,i) for i in range(1,cnt1+1,2))*pow(2,cnt0)
else:
    res = sum(C(cnt1,i) for i in range(0,cnt1+1,2))*pow(2,cnt0)
print(res)