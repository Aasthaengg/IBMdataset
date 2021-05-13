n,k=map(int,input().split())
d=[0]*(k+1)
mod=10**9+7
ans=0
for i in range(1,k+1)[::-1]:
    tmp=0
    c=0
    for j in range(i,k+1,i):
        c+=1
        tmp+=d[j]
    d[i]=pow(c,n,mod)-tmp
    ans=(ans+d[i]*i)%mod
print(ans)