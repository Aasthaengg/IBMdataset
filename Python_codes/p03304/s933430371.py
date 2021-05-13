n,m,d=map(int,input().split())
if d==0:print((m-1)/n)
else:
    if d<=n//2:
        print((2*n-2*d)/(n**2)*(m-1))
    else:
        print((m-1)/n)
