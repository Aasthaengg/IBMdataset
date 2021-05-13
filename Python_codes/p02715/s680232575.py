n,k = map(int,input().split())
MOD = 10**9 + 7

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


yaku = [0]*(k+1)
for i in range(1,k+1):
    yaku[i] = k // i
am = [0]*(k+1)
for i in range(1,k+1):
    am[i] = pk(yaku[i],n,MOD)
    
newam = [0]*(k+1)
for i in range(k,0,-1):
    newam[i] = am[i]
    for j in range(i*2,k+1,i):
        newam[i] = ((newam[i] + MOD) - newam[j]) % MOD
        
ans = 0
for i in range(1,k+1):
    ans = (ans + (newam[i]*i)) % MOD
    
print(ans)