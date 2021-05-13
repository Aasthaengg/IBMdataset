import sys
mod=10**9+7
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))


if a[0]>b[0] or b[n-1]>a[n-1]: print(0);sys.exit()
elif n<=2: print(1);sys.exit()

ans=1
for i in range(1,n-1):
    if a[i]==a[i-1] and b[i]==b[i+1]:
        ans=ans*min(a[i],b[i])%mod
    else:
        if a[i]!=a[i-1] and a[i]>b[i]: print(0);sys.exit()
        if b[i]!=b[i+1] and b[i]>a[i]: print(0);sys.exit()
print(ans)