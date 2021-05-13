n,m,d = map(int, open(0).read().split())
if d == 0:
    print((n*(m-1))/pow(n,2))
else:
    print((2*(m-1)*(n-d))/pow(n,2))