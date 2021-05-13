n,t=map(int,input().split())
a=list(map(int,input().split()))
accum=[0]*n
accum[n-1]=a[n-1]
for i in reversed(range(1,n)):
    accum[i-1]=max(accum[i],a[i-1])
maxi=0
for i in range(n-1):
    maxi=max(maxi,accum[i+1]-a[i])
ans=0
d={}
for i in range(n):
    if a[i]-maxi>0:
        if a[i]-maxi in d:
            if d[a[i]-maxi]>0:
                d[a[i]-maxi]-=1
                ans+=1
    if a[i] not in d:
        d[a[i]]=1
    else:
        d[a[i]]+=1
print(ans)