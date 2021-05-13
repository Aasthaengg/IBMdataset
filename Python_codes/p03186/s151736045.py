a,b,c = map(int, input().split())
if a+b+1 < c:
    print(a+2*b+1)
else:
    print(c+b)