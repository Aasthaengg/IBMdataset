n, k = map(int, input().split())
mod = 10**9+7

def cmb1(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

mod = 10**9+7 #出力の制限
N = 10**5+50
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

ans = [0]*k
for i in range(1, k+1):
    ans[i-1] = cmb1(n-k+1, i, mod)*cmb1(k-1, i-1, mod)
    ans[i-1] %= mod
for i in range(k):
    print(ans[i])
