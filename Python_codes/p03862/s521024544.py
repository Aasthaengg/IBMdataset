n,x=map(int,input().split())

a=list(map(int,input().split()))

c=0

for i in range(n-1):
    if a[i]+a[i+1]>x:
        c+=a[i]+a[i+1]-x
        if x-a[i]>=0:
            a[i+1]=x-a[i]
        else:
            a[i+1]=0
            a[i]=x

print(c)