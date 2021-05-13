import collections
n=int(input())
a=list(map(int,input().split()))
mod=10**9+7
a.sort()

if n%2==0:
    if a[0]!=1:
        print(0)
        exit()
    for i in range(n-1):
        if (i%2==0 and a[i]!=a[i+1]) or i%2==1 and (a[i+1]-a[i]!=2):
            print(0)
            exit()
else:
    if a[0]!=0:
        print(0)
        exit()
    for g in range(1,n-1):
        if (g%2==1 and a[g]!=a[g+1]) or g%2==0 and (a[g+1]-a[g]!=2):
            print(0)
            exit()

print(2**(n//2)%mod)