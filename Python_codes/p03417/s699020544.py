n,m=map(int,input().split())
if n>=2 and m>=2:
    print((m-2)*(n-2))
elif n==1:
    if m==1:
        print(1)
    else:
        print(m-2)
elif m==1:
    if n==1:
        print(1)
    else:
        print(n-2)
