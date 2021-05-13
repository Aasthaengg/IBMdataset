k = int(input())
s = input()

# nCr(n, r, m)
mod = 1000000007
n = len(s) + k

fac = [1,1] # 階乗 n!
inv = [0,1] # 逆元 1/n
finv = [1,1] # 逆元の階乗 (n^-1)! = (1/n)!

for i in range(2, n+1):
    fac.append( (fac[-1] * i ) % mod )
    inv.append( (-inv[mod%i] * (mod//i)) % mod )
    finv.append( (finv[-1] * inv[-1]) % mod )

def nCr(n, r, m):
    if (n<0 or r<0 or n<r): return 0
    r = min(r, n-r)
    return fac[n] * finv[n-r] * finv[r] % m

# a^n mod m
def modpow(a, n, m):
    x = 1
    while n > 0:
        if n & 1: x = x * a % m
        a = a * a % m
        n >>= 1
    return x

n = len(s)
ans = 0
for i in range(k+1):
    ans += modpow(25, i, mod) * modpow(26, k-i, mod) * nCr(i+n-1, n-1, mod)
    ans %= mod
print(ans)
