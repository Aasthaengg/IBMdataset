n, k = map(int, input().split())
r = n - k

def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

mod = 10**9+7 #出力の制限
N = 10**4
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )


for i in range(1, k+1):
    if i == 1:
        num = r + 1
    else:
        r_ball = r - (i - 1)
        num_1 = cmb(r_ball+i, i, mod)
        num_2 = cmb(k-1, i-1, mod)
        num = (num_1 * num_2) % mod
    print(num)


