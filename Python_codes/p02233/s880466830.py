def g(a,b,n):
    if n==1:return a
    else:return g(a+b,a,n-1)
print(g(1,1,int(input())))