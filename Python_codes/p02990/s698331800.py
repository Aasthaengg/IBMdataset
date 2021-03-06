n,k = map(int,input().split())
def cmb(n, k, mod, fac, ifac):    
    k = min(k, n-k)
    return fac[n] * ifac[k] * ifac[n-k] % mod

def make_tables(mod, n):
    fac = [1, 1] # 階乗テーブル・・・(1)
    ifac = [1, 1] #逆元の階乗テーブル・・・(2)
    inverse = [0, 1] #逆元テーブル・・・(3)
    for i in range(2, n+1):
        fac.append((fac[-1] * i) % mod)
        inverse.append((-inverse[mod % i] * (mod//i)) % mod)
        ifac.append((ifac[-1] * inverse[-1]) % mod)
    return fac, ifac

mod = 1000000007
fac, ifac = make_tables(mod, n)

r = n - k
for i in range(k):
    if r+1 >= i+1:
        ans = cmb(k-1, i, mod, fac, ifac)
        ans *= cmb(r+1, i+1, mod, fac, ifac)
        print(ans%mod)
    #ans = (k-1Ci)*(r+1Ci+1)
    else:
        print(0)
