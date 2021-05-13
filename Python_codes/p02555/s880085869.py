S = int(input())
MOD = 10**9 + 7

class Combination:
    #クラス外にMODの宣言をする必要がある。
    def __init__(self, N):
        self.fac = [1] * (N + 1)
        for i in range(1, N + 1):
            self.fac[i] = (self.fac[i - 1] * i) % MOD
        self.invmod = [1] * (N + 1)
        #逆元?
        self.invmod[N] = pow(self.fac[N], MOD - 2, MOD)
        for i in range(N, 0, -1):
            self.invmod[i - 1] = (self.invmod[i] * i) % MOD

    def calc(self, n, k):  # nCk
        return self.fac[n] * self.invmod[k] % MOD * self.invmod[n - k] % MOD


N = S // 3
com = Combination(10**6)
ans = 0
for n in range(1,N+1):
    s = S - 3*n
    ans = (ans+com.calc(s+n-1,n-1))%MOD
print(ans)