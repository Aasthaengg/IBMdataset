a,b,c = map(int,input().split())
if (a*b*c)%2 == 1:
    print(min(a*b,b*c,a*c))
else:
    print(0)