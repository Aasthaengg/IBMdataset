K=int(input())
S=input()
N=len(S)

F = 2*10**6+5
mod = 10**9+7
fact = [1]*F
inv = [1]*F
for i in range(2,F):
    fact[i]=(fact[i-1]*i)%mod
inv[-1]=pow(fact[-1],mod-2,mod)
for i in range(F-2,1,-1):
    inv[i] = (inv[i+1]*(i+1))%mod

def comb(n,k):
    ans=(fact[n]*inv[n-k])%mod
    return (ans*inv[k])%mod

ans=0

select=pow(25,K,mod)
inv25=inv[25]*fact[24]

for i in range(K+1):
    ans+=select*comb(N-1+K-i,N-1)
    ans%=mod
    select*=inv25*26
    select%=mod

print(ans)

