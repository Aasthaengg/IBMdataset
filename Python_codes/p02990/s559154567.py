def comInit(MOD, n):
    fact=[1,1] # fact[n]はnの階乗
    invr=[0,1] # invr[n]はnの逆元
    invr_fact=[1,1] # invr_fact[n]は逆元の階乗

    for i in range(2,n+1):
        fact.append(fact[-1]*i%MOD)
        invr.append(-invr[MOD%i]*(MOD//i)%MOD)
        invr_fact.append(invr_fact[-1]*invr[-1]%MOD)
    return fact,invr_fact

def calCom(n,k,MOD,fact,invr_fact):
    k=min(k,n-k)
    return fact[n]*invr_fact[k]*invr_fact[n-k]%MOD

n,k = map(int,input().split())
mod = 10**9+7
dp = [None] * min(n-k+1,k)
dp[0] = (1 * (n-k+1)) % mod
print(dp[0])
f,inv = comInit(mod,n)
for i in range(1,k):
    if i>k-1 or n-k<i:
        print(0)
        continue
    print((calCom(k-1,i,mod,f,inv) * calCom(n-k+1,i+1,mod,f,inv))%mod)
