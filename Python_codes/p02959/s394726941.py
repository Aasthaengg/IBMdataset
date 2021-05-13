n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ans=0
for i in range(n):
    if b[i]<=a[i]:
        ans=ans+b[i]
    elif b[i]<=a[i]+a[i+1]:
        ans=ans+b[i]
        a[i+1]=a[i]+a[i+1]-b[i]
    else:
        ans=ans+a[i]+a[i+1]
        a[i+1]=0
print(ans)