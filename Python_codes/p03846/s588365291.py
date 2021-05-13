import sys
mod=10**9+7
n=int(input())
a=list(map(int,input().split()))
a.sort()
if n%2:#odd
    if a[0]!=0:
        print(0)
        sys.exit()
    cur=2
    for i in range(1,n,2):
        if a[i]!=cur or a[i]!=a[i+1]:
            print(0)
            sys.exit()
        cur+=2
    ans=1
    for i in range(n//2):
        ans=(ans*2)%mod
    print(ans)
else:#even
    cur=1
    for i in range(0,n,2):
        if a[i]!=cur or a[i]!=a[i+1]:
            print(0)
            sys.exit()
        cur+=2
    ans=1
    for i in range(n//2):
        ans=(ans*2)%mod
    print(ans)

