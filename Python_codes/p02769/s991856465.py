def cmb(n, r):#コンビネーション(mod)の高速計算　
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod
mod = 10**9+7 #出力の制限
N = 5*10**5 #Nの最大値
g1 = [0]*(N+1) #元テーブル(p(n,r))
g1[0] = g1[1] = 1
g2 = [0]*(N+1) #逆元テーブル
g2[0] = g2[1] = 1
inverse = [0]*(N+1) #逆元テーブル計算用テーブル
inverse[0],inverse[1] = 0,1
for i in range(2,N+1):
    g1[i] = (g1[i-1] * i) % mod
    inverse[i] = (-inverse[mod % i] * (mod//i)) % mod
    g2[i] = (g2[i-1] * inverse[i]) % mod

n,k = map(int,input().split())

# 0の数がi個の場合の数
dp = [0]*(n+1)
# 残りn-i種類にi個を割り振る　×　0がi個の場合の数 -> n-1Ci * nCi
for i in range(n+1):
    dp[i] = cmb(n-1,i) * cmb(n,i) % mod

if k == 1:
    ans = dp[1]
else:
    k = min(n,k)
    ans = 0
    for i in range(k+1):
        ans += dp[i]
        ans %= mod
print(ans)