a,b,c,d=map(int,input().split())
if a*b!=c*d:
    print(max(a*b,c*d))
else:
    print(a*b)