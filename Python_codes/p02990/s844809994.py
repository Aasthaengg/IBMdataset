n, k = map(int, input().split())
nb = k
nr = n-k
mod = 10**9+7
fac = [1] * 2001
fac_inv = [1] * 2001
for i in range(1,2001):
    fac[i] = (fac[i-1] * i) %mod
    fac_inv[i] = pow(fac[i], mod-2, mod)

# 足してa個をb分割する場合の数(順序考慮)が分かればいい
def f(a,b):
    if (a == 0) & (b==0):
        return 1
    if b <= 0:
        return 0
    if b > a:
        return 0
    res = fac[a-1] * fac_inv[b-1] * fac_inv[a-b] %mod
    return res

cnt = 0    
for i in range(1,k+1): # blue 1～k
    fnbi = f(nb, i)
    cnt = f(nr, i-1) * fnbi \
           + 2 * f(nr, i) * fnbi\
           + f(nr, i+1) * fnbi
    cnt = cnt%mod
    print(cnt)
