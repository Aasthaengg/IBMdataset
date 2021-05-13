n,m,d = map(int,input().split())
if d==0:
    print((1*n-2*d)*(m-1)/n**2)
elif n>=2*d:
    print((2*n-2*d)*(m-1)/n**2)
else:
    print(2*d*(m-1)/n**2)