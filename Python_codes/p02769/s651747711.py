def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

mod = 10**9+7 #出力の制限
N = 10**6
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

N, K = map(int, input().split())
MOD = 10**9+7
n = min(N,K)
ans = 0
for i in range(max(1,N-n),N+1):
  m = cmb(N,i,MOD)
  m *= cmb(N-1,i-1, MOD)
  ans += m
  ans %= MOD
print(ans)