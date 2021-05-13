n,m,d = map(int,input().split())
if d == 0:
    print((m-1)/n)
else:
    x = max(0,n-2*d)
    ans = (x*2+2*d)/n/n*(m-1)
    print(ans)