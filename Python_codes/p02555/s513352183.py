n=int(input())
mod=10**9+7
if n<3:
    print(0)


else:
    a=[0]*(n)
    a[0]=0
    a[1]=0
    a[2]=1
    for i in range(3,n):
        a[i]=(a[i-3]+a[i-1])%mod
    print(a[n-1])