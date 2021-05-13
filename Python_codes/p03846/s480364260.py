#050_C
n=int(input())
a=sorted(list(map(int,input().split())))
mod=10**9+7

if n%2:
    if all(-(-i//2)*2==a[i] for i in range(n)):
        print(pow(2,n//2,mod))
    else:
        print(0)
else:
    if all((i//2)*2+1==a[i] for i in range(n)):
        print(pow(2,n//2,mod))
    else:
        print(0)