n,x=map(int,input().split())
a=list(map(int,input().split()))
asum=[0]*(n-1)
for i in range(n-1):
    asum[i]+=(a[i]+a[i+1])
temp=0
for j in range(n-1):
    if asum[j]>=x:
        if j!=n-2:
            asum[j+1]-=min(a[j+1],(asum[j]-x))
        temp+=(asum[j]-x)
            
print(temp)