n,k=map(int,input().split())
mod=10**9+7
fact=[1]*(max(n-k,k)+2)
inv=[1]*(max(n-k,k)+2)
for i in range(2,max(n-k,k)+2):
    fact[i]=i*fact[i-1]%mod
inv[-1]=pow(fact[-1],mod-2,mod)
for i in range(max(n-k,k)+1,1,-1):
    inv[i-1]=inv[i]*i%mod
def comb(x,y):return fact[x]*inv[y]%mod*inv[x-y]%mod if x>=y>=0 else 0
for i in range(1,k+1):
    print(comb(k-1,i-1)*comb(n-k+1,i)%mod)