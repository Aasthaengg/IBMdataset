def factorize(n):
    fct = []
    
    for i in range(2, int(n**0.5)+1):
        c = 0
        
        while n%i==0:
            n //= i
            c += 1
            
        if c>0:
            fct.append((i, c))
    
    if n>1:
        fct.append((n, 1))
    
    return fct
    
MAX = 10**5+100
MOD = 10**9+7
fact = [0]*MAX #fact[i]: i!
inv = [0]*MAX #inv[i]: iの逆元
finv = [0]*MAX #finv[i]: i!の逆元
fact[0] = 1
fact[1] = 1
finv[0] = 1
finv[1] = 1
inv[1] = 1
    
for i in range(2, MAX):
    fact[i] = fact[i-1]*i%MOD
    inv[i] = MOD-inv[MOD%i]*(MOD//i)%MOD
    finv[i] = finv[i-1]*inv[i]%MOD

def C(n, r):
    if n<r:
        return 0
    if n<0 or r<0:
        return 0
    return fact[n]*(finv[r]*finv[n-r]%MOD)%MOD

N, M = map(int, input().split())
fct = factorize(M)
ans = 1

for _, c in fct:
    ans *= C(N-1+c, c)
    ans %= MOD

print(ans)