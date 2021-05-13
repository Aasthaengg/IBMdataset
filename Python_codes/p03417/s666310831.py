n,m=map(int,input().split())
if  n<=2 and m<=2:
    if n==m==1:
        print(1)
    else:
        print(0)
elif n==1 or m==1:
    print(max(n,m)-2)
elif n==2 or m==2:
    print(0)
else:
    print((n-2)*(m-2))