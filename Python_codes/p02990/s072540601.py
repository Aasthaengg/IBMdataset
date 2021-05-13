n,k=map(int,input().split())

F = 10000
mod = 10**9+7
fact = [1]*F
inv = [1]*F
for i in range(2,F):
    fact[i]=(fact[i-1]*i)%mod
inv[F-1]=pow(fact[F-1],mod-2,mod)
for i in range(F-2,1,-1):
    inv[i] = (inv[i+1]*(i+1))%mod

def comb(n,k):
    ans=(fact[n]*inv[n-k])%mod
    return (ans*inv[k])%mod
def H(n,k):
    return comb(n+k-1,k)

for i in range(1,k+1):
    if i<=n-k+1:
        print(comb(n-k+1,i)*H(i,k-i)%mod)
    else:
        print(0)