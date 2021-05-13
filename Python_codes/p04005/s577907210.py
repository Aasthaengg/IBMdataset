a,b,c=map(int,input().split())
if a%2 == 0 or b%2 == 0 or c%2 == 0:
    print(0)
else:
    x = max(a,b,c)
    y = min(a,b,c)
    z = a+b+c -(x+y)
    print(y*z)