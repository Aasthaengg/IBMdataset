n,k=map(int,input().split())
mod=10**9+7
dp=[pow(k//i,n,mod) for i in range(1,k+1)]
exactly=[0]*k
for i in range(k,0,-1):
    f=0
    for j in range(2*i,k+1,i):
        f+=exactly[j-1]
    exactly[i-1]=dp[i-1]-f
    exactly[i-1]%=mod
print(sum(i*exactly[i-1]%mod for i in range(1,k+1))%mod)