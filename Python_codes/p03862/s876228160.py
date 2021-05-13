n,x=map(int,input().split())
a=list(map(int,input().split()))
ans=0
for i in range(n):
    if a[i]>x:
        ans+=a[i]-x
        a[i]=x
for i in range(n-1):
    b=a[i]+a[i+1]
    if b>x:
        ans+=b-x
        a[i+1]-=b-x
print(ans)