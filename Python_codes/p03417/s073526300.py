n,m=map(int,input().split())
if n==1:
    if m==1:
        print(1)
    else:
        print(m-2)
else:
    if m==1:
        print(n-2)
    else:
        print((n*m)-((n+m)*2-4))
