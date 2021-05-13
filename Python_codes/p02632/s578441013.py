k = int(input())
s = input()
n = len(s)
mod = 10**9+7
def cmb(n,r,mod):
    r = min(r, n-r)
    return (fact[n] * factinv[r] * factinv[n-r]) % mod
def makefact(n,mod):
    fact = [1,1]
    factinv = [1,1]
    inv = [0,1]
    for i in range(2,n+1):
        fact.append((fact[-1]*i) % mod)
        inv.append(-inv[mod%i]*(mod//i)%mod)
        factinv.append((factinv[-1]*inv[-1])%mod)
    return fact,factinv
fact,factinv = makefact(2*10**6+5,mod)
ans = 0
for i in range(k+1):
    temp = pow(26,i,mod)
    c = cmb(n+k-i-1,n-1,mod)
    temp *= c*pow(25,k-i,mod)
    ans = (ans+temp)%mod
print(ans)