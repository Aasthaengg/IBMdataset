n,k=map(int,input().split())
x_max=(n//k)
a=n-k*x_max
b=abs(a-k)
print(min(a,b))