n,a,b=map(int,input().split())
c,d=divmod(n,a+b)
print(c*a+min(a,d))