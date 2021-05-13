n,m,k = map(int,input().split())
MOD = 998244353

def pk(x,n,mod):
    if n == 0:
        return 1

    K = 1
    while n > 1:
        if n % 2 != 0:
            K = K * x % mod
        x = x ** 2 % mod
        n //= 2

    return K * x % mod

nck = [0]*n
kake = [0]*n

a = m
for i in range(n):
    kake[i] = a
    a = a*(m-1)%MOD
    
a = 1
for i in range(n):
    nck[i] = a
    a = int(a * (n-1-i) * pk(i+1,MOD-2,MOD)) % MOD
    
ans = 0
for i in range(k+1):
    ans = (ans + (nck[i] * kake[n-1-i] % MOD)) % MOD
    
print(ans)