n,k=map(int,input().split())
if k%2==0:
    x=(n+k/2)//k
    y=n//k
    print(int(x**3+y**3))
else:
    x=n//k
    print(int(x**3))
