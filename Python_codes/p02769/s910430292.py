n,m=map(int,input().split())
mod=10**9+7

def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

p = mod
N = 4 * 10 ** 6 + 10 # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用
 
for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)
    
def shikiri(a,b):
    return fact[a+b]*factinv[a]*factinv[b]%mod

ans=0
for i in range(min(n,m+1)):
    ans+=shikiri(n-1-i,i)*cmb(n,i,p)
    #print(ans)
    ans%=mod

if m==1:
    ans-=1
print(ans)