a,b,c = map(int, input().split())
m = max(a,b,c)
if (3*m-(a+b+c))%2 == 0:
    t = 3*m-(a+b+c)
    print(t//2)
else:
    t = 3*(m+1)-(a+b+c)
    print(t//2)