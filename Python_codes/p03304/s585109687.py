n,m,d=map(int,input().split())

if n>=2 and d>=1:
    print(2*(n-d)*(m-1)/(n*n))
elif d==0:
    print((m-1)/n)
