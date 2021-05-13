a,b,c = map(int,input().split())
if any([i%2 == 0 for i in (a,b,c)]):
    print(0)
else:
    print(min(b*c,c*a,a*b))