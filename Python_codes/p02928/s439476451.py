n,k=map(int,input().split())
*a,=map(int,input().split())

mod=10**9+7
ans=0
cnt=0
for i in range(n):
    for j in range(i+1,n):
        ans+=k if a[i]>a[j] else 0
        cnt+=0 if a[i]==a[j] else 1

ans%=mod
ans+=(cnt*k*(k-1)//2)
ans%=mod


print(ans)