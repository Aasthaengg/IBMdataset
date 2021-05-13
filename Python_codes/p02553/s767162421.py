a,b,c,d=map(int,input().split())
if a*c>a*d:
    if b*c>b*d:
        if a*c>b*c:
            print(a*c)
        else:
            print(b*c)
    else:
        if a*c>b*d:
            print(a*c)
        else:
            print(b*d)
else:
    if b*c>b*d:
        if a*d>b*c:
            print(a*d)
        else:
            print(b*c)
    else:
        if a*d>b*d:
            print(a*d)
        else:
            print(b*d)