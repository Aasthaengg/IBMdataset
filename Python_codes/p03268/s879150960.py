n,k=map(int,input().split())
if k%2==1:
    a=n//k
    print(a**3)
else:
    a=k//2
    b=n//a
    print((b//2)**3+((b+1)//2)**3)