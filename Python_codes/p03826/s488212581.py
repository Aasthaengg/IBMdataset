a,b,c,d = (int(x) for x in input().split())
if a*b>=c*d:
    print(a*b)
else:
    print(c*d)