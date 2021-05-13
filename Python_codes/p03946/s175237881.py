n,t=map(int,input().split())
a=[int(i) for i in input().split()]
mn,mx=10**10,-1
d={}
for i in range(n-1):
    mn=min(a[i],mn)
    mx=max(a[i+1]-mn,mx)
    d[a[i]]=i
d[a[n-1]]=n-1
ans=0
for i in range(1,n):
    if a[i]-mx in d and d[a[i]-mx]<i:
        ans+=1
print(ans)
