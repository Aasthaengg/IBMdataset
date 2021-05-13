n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
if n==1:
    print(int(a==b))
    exit()
mod=10**9+7
INF=10**9+1 
u=[INF]*n
d=[1]*n
u[0]=a[0]
d[0]=a[0]
for i in range(1,n):
    if a[i]-a[i-1]:
        d[i]=a[i]
    u[i]=a[i]
u[-1]=b[-1]
d[-1]=b[-1]
for i in range(n-2,-1,-1):
    if b[i]-b[i+1]:
        if b[i]<d[i] or b[i]>u[i]:
            print(0)
            exit()
        d[i]=b[i]
    u[i]=min(b[i],u[i])
ans=1
for i in range(n):
    ans=ans*(u[i]-d[i]+1)%mod
print(ans)