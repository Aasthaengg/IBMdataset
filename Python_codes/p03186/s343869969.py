a,b,c = map(int,input().split())
if c < a+b:
    print(b+c)
elif c > a+b:
    print(a+b+b+1)
else:
    print(c+b)