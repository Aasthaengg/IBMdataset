k=int(input())
s=input()
ans=0
mod=1000000007
x=2200000
fact=[0]*x
invfact=[0]*x
fact[0]=1
for i in range(1,x):
    fact[i]=fact[i-1]*i%mod
invfact[x-1]=pow(fact[x-1],mod-2,mod)
for i in range(x-2,-1,-1):
    invfact[i]=invfact[i+1]*(i+1)%mod
def nCk(n,k):
    return(fact[n]*invfact[k]*invfact[n-k])%mod
for i in range(0,k+1):
    # print(nCk(len(s)+i-1,i),pow(25,i,mod),pow(26,k-i,mod))
    ans+=nCk(len(s)+i-1,i)*pow(25,i,mod)*pow(26,k-i,mod)
print(ans%mod)