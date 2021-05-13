a,b,x=(int(x) for x in input().split())

if a==0:
    print(1+b//x)
else:
    c=b//x-(a-1)//x
    print(c)
