n,m=map(int,input().split())
a=list(map(int,input().split()))
a[0]%=m
for i in range(n-1):
    a[i]%=m
    a[i+1]+=a[i]
    a[i+1]%=m
d=dict()
ans=0
for i in range(n):
    if a[i]==0:
        ans+=1
    if a[i] not in d:
        d[a[i]]=1
    else:
        ans+=d[a[i]]
        d[a[i]]+=1
print(ans)