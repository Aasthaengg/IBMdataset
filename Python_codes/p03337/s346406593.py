a,b=map(int,input().split())
x=a+b
y=a-b
z=a*b
if x>=y and x>=z:
    print(x)
elif y>=x and y>=z:
    print(y)
else:
    print(z)