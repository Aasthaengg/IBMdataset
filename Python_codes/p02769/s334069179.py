class Cmb:
    def __init__(self, N, mod=10**9+7):
        self.fact = [1,1]
        self.fact_inv = [1,1]
        self.inv = [0,1]
        
        """ 階乗を保存する配列を作成 """
        for i in range(2, N+1):
            self.fact.append((self.fact[-1]*i) % mod)
            self.inv.append((-self.inv[mod%i] * (mod//i))%mod)
            self.fact_inv.append((self.fact_inv[-1]*self.inv[i])%mod)
    
    """ 関数として使えるように、callで定義 """
    def __call__(self, n, r, mod=10**9+7):
        if (r<0) or (n<r):
            return 0
        r = min(r, n-r)
        return self.fact[n] * self.fact_inv[r] * self.fact_inv[n-r] % mod

n,k = map(int,input().split())
mod = 10**9+7
c = Cmb(N=n)
ans = 0
for l in range(min(k+1, n)):
    tmp = c(n,l)*c(n-1, n-l-1)
    ans += tmp%mod
print(ans%mod)