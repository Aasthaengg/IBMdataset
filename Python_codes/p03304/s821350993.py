n, m, d = (float(i) for i in input().split())
if d ==0:
    print((m-1)/n)
else:
    x =(2*n-2*d)*(m-1)/n**2
    print(x)