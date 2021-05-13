n,a,b=map(int,input().split())
x=n//(a+b)*a
y=n%(a+b)
if y<a:
    print(x+y)
else:
    print(x+a)