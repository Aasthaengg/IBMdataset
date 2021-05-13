a, b, c = map(int, input().split())
if a >= b and a >= c:
    print(int(str(a)+str(b)) + c)
elif b >= a and b >= c:
    print(int(str(b)+str(a)) + c)
else:
    print(int(str(c)+str(a)) + b)
