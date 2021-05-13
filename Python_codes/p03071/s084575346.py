a,b=map(int,input().split())
if a-1>=b:
    print(2*a-1)
elif b-1>=a:
    print(2*b-1)
else :
    print(a+b)