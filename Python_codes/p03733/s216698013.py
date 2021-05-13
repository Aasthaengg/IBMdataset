n,T=map(int,input().split())
L=list(map(int,input().split()))
ans=T
for i in range(1,n):
    if L[i]-L[i-1]<T:
        ans+=L[i]-L[i-1]
    else:ans+=T
print(ans)