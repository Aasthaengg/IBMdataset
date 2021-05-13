#132
N,K = map(int, input().split())
MOD_BY = 7 + 10**9

##############################################
#https://tane-no-blog.com/976/
mod = pow(10, 9) + 7

def comb(N, x):
    #n*(n-1)*…*(n-1+1)を計算
    numerator = 1
    for i in range(N-x+1, N+1):
        numerator = numerator * i % mod
        
    #a!を計算
    denominator = 1
    for j in range(1, x+1):
        denominator = denominator * j % mod
        
    #最後の項 a!**((10**9+7)-2)を計算
    d = pow(denominator, mod-2, mod)
    return numerator * d
##############################################

ans = 0

for i in range(1,K+1):
    #青球のグループ分けの個数
    #(K-1)C(i-1)
    #bxbxbxbxbxbxb …xから分割数-1を選ぶ
    
    #赤玉への挿入箇所の個数
    #(N-K+1)C(i)
    #xrxrxrxrxrx …xから分割数分を選ぶ
    ans = comb(K-1,i-1)*comb(N-K+1,i)%MOD_BY
    print(ans) 