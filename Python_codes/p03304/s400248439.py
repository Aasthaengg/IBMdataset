n,m,d = map(int,input().split())
if d == 0:
    print((m-1)/n)
else:
    a = 2*(n-d)/(n**2)
    print(a*(m-1))