n,k=map(int, input().split())  
MOD=10**9+7
uplimit=2*10**5+1
fac = [0 for i in range(uplimit)] # 階乗
inv = [0 for i in range(uplimit)] # iの逆元 
finv = [0 for i in range(uplimit)] # i!の逆元

def fac_and_inv() :
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1
    for i in range(2, uplimit) :
        fac[i] = fac[i-1] * i % MOD
        inv[i] = MOD - inv[MOD%i] * int(MOD / i) % MOD
        finv[i] = finv[i-1] * inv[i] % MOD
    return fac, finv, inv

temp = fac_and_inv()
ans = 0

#  x : 0人部屋の数
for x in range(0, k+1) : # k回動ける=最大kまで0人部屋になりうる
    if(x >= n) : # kがn以上の場合を想定。これ以降は計算する意味なし。
        break
    y = n - x # y : 人がいる部屋の数
    ans += (fac[n]*finv[x]*finv[n-x]) * (fac[n-1] * finv[x] * finv[y-1]) % MOD
    # 要はnCx * n-xHx 通り
    # nCxは0人部屋の選び方
    # n-xHxは n-xから重複を許してx選ぶ組み合わせ
    # n-xHx = n-1Cn-x-1 = n-1Cy-1
    # よって(n-1)! / x! / (y-1)!が欲しい

print(ans % MOD)

