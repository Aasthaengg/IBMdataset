n,t=map(int,input().split())
a=list(map(int,input().split()))
min=[float("inf")]*n
min[0]=a[0]
m=0
for i in range(1,n):
    if min[i-1]>a[i]:
        min[i]=a[i]
    else:
        min[i]=min[i-1]
for i in range(n):
    r=a[i]-min[i]
    m=max(r,m)
ans=0
for i in range(n):
    r=a[i]-min[i]
    if r==m:
        ans+=1
print(ans)
