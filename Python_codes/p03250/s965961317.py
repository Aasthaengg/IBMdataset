a,b,c=map(int,input().split())
if a>=b>=c or a>=c>=b:
    print(10*a+b+c)
elif c>=a>=b or c>=b>=a:
    print(10*c+a+b)
else:
    print(10*b+a+c)