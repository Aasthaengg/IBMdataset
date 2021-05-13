n, k = map(int, input().split())
mod = 10**9+7

def pow(x, n):
    ans = 1
    if n in dict:
        return dict[n]
    n_tmp = n
    while n:
        if n % 2:
            ans *= x
            ans %= mod
        x *= x
        n >>= 1
    dict[n_tmp] = ans
    return ans

def cmb(n, r, mod):
    if (r<0 or r>n):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range(2, n+1):
    g1.append( (g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

ans = 0
for i in range(k):
    # print(cmb(n-k+1, i+1, mod), cmb(k-1, i, mod))
    tmp_ans = cmb(n-k+1, i+1, mod)
    tmp_ans %= mod
    tmp_ans *= cmb(k-1, i, mod)
    tmp_ans %= mod
    print(tmp_ans)
