n,m=map(int,input().split())
if n>=2 and m>=2:
    print(n*m-2*(n+m-2))
else:
    if not (n==1 and m==1):
        print(n+m-3)
    else:
        print(1)