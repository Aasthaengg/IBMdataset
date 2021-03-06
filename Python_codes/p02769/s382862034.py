n,k = list(map(int, input().split()))
mod = int(1e9+7)



def init_cmb(Nmax):
    #mod = 10**9+7 #出力の制限
    g1 = [1, 1] # 元テーブル
    g2 = [1, 1] # 逆元テーブル
    inverse = [0, 1] #逆元テーブル計算用テーブル

    for i in range(2, Nmax + 1):
        g1.append((g1[-1] * i) % mod)
        inverse.append((-inverse[mod % i] * (mod//i)) % mod)
        g2.append((g2[-1] * inverse[-1]) % mod)
    return g1, g2

g1,g2 = init_cmb(n+10)

def cmb(n, r, modn=mod):
    if (r < 0 or r > n):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % modn
  
# ci = 0 である個数が m となるような数列の数は、 nCm ×n−m Hm = nCm * n-1Cn-m-1
# 0 <= m < n で足算する

ans = 0
for i in range(min(k+1,n)):
  wk = cmb(n,i) * cmb(n-1, n-i-1) % mod
  ans = (ans + wk ) % mod
  
print(ans)