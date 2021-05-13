a,b=map(int,input().split())

c=min(a,b)

if a==c:
    a=str(a)
    print(a*b)
else:
    b=str(b)
    print(b*a)