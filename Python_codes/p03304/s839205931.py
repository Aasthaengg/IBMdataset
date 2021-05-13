n,m,d = map(int,input().split())

if d == 0:
    print((n-d)*(m-1)/(n**2))
else:
    print((n-d)*2*(m-1)/(n**2))

