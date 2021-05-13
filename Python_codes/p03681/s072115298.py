n,m=list(map(int,input().split()))
mod=10**9+7

if abs(n-m)>1:
    print(0)
    exit(0)

if abs(n-m)==1:
    ans=1
else:
    ans=2

while n>0:
    ans*=n
    ans%=mod
    n-=1

while m>0:
    ans*=m
    ans%=mod
    m-=1

print(ans)