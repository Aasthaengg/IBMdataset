k = int(input())
s = input()
n = len(s)
MOD = 10**9+7
ans = 0

fact = [1] * 2200000
invfact = [1] * 2200000
 
for i in range(1, 2200000):
    fact[i] = fact[i-1] * i % MOD
 
invfact[2200000 - 1] = pow(fact[2200000 - 1], MOD-2, MOD)
 
for i in range(2200000-1, 0, -1):
    invfact[i-1] = invfact[i] * i % MOD

def comb(n, k):
    return fact[n] * invfact[k] * invfact[n-k] % MOD

for i in range(k+1):
    b = pow(26, k-i, MOD)
    b *= pow(25, i, MOD)
    b *= comb(i+n-1, n-1)
    ans += (b % MOD)
    
print(ans%MOD)