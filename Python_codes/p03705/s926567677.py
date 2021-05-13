n,a,b=map(int,input().split())
if a>b:
    print(0)
elif n==1 and a!=b:
    print(0)
elif n==1:
    print(1)
elif n==2:
    print(1)
else:
    if a==b:
        print(1)
    else:
        n-=2
        print((b-a)*n+1)
