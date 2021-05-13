n,m = map(int,input().split())
l = []
i = 2
if m == 1 or n == 1:
    print(1)
    exit()
while m != 1:
    if m%i == 0:
        l.append(0)
        while m%i == 0:
            l[-1] += 1
            m //= i
    i += 1

mod = 10**9+7 
fact = [1,1]
finv = [1,1]
inv = [0,1]
 
for i in range(2,n+max(l)+5):
    fact.append((fact[-1]*i)%mod)
    inv.append((inv[mod%i]*(mod-mod//i))%mod)
    finv.append((finv[-1]*inv[-1])%mod)
 
def nCr(n,r,mod):
    if r > n:
        return 0
    else: 
        return fact[n]*finv[r]*finv[n-r]%mod

ans = 1

for i in l:
    ans *= nCr(n+i-1,n-1,mod)
    ans %= mod
print(ans)