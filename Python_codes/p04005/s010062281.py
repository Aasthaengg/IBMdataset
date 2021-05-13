a,b,c = map(int, input().split())
if max(a,b,c)%2 == 0:
    print(0)
else:
    big = (((max(a,b,c)//2)+1)*a*b*c)//max(a,b,c)
    small = ((max(a,b,c)//2)*a*b*c)//max(a,b,c)
    print(big-small)