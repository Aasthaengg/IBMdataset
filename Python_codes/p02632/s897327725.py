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

i25, i26 = [1], [1]
for _ in range(k):
    i25.append(i25[-1] * 25 % mod)
    i26.append(i26[-1] * 26 % mod)

n = len(s)
ans = 0
for i in range(k+1):
    ans += i25[i] * i26[k-i] * nCr(i+n-1, n-1, mod)
    ans %= mod
print(ans)
