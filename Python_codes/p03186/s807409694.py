a,b,c = map(int,input().split())
d = a + b

if d >= c:
    print(b + c)
else:
    print(b + c - (c - d) + 1)
