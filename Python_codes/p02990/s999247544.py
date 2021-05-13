n,k=map(int, input().split())
mod=10**9+7
def conbi(n,r,mod):
    ue=1
    for i in range(n-r+1,n+1):
        ue*=i
        ue%=mod
 
    sita=1
 
    for i in range(1,r+1):
        sita*=i
        sita%=mod
 
    sita=pow(sita,mod-2,mod)
 
    return (ue*sita)%mod
for i in range(1,k+1):
    ans=conbi(n-k+1,i,mod)*conbi(k-1,i-1,mod)
    print(ans%mod)
