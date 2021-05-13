a,b,c = map(int,input().split())
if b >= c:
    print(c+b)
elif b < c and c <= a + b:
    print(b+c)
elif a+b < c:
    print(b + b + a + 1)
 