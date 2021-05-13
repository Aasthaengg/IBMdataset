n,m=map(int,input().split())
a=0
b=0
if n!=1:
    a=(n*(n-1))/2
if m!=1:
    b=(m*(m-1))/2
c=int(a+b)
print(c)
