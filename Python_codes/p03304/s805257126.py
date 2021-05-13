n,m,d = map(int,input().split())
if d != 0:
    print((2*n-2*d)*(m-1)/pow(n,2))
if d == 0:
    print(n*(m-1)/pow(n,2))
