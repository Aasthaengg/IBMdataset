n,k=map(int,input().split())
if k%2==1:
    print((n//k)**3)
else:
    kk=k//2
    print((n//k)**3+((n+kk)//k)**3)