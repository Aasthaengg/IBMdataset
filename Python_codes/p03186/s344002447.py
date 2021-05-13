a, b, c= map(int, input().split())
if c-1<=b:
    print(c+b)
elif a+b<=c-1:
    print(a+b+b+1)
elif a+b>=c:
    print(b+c)