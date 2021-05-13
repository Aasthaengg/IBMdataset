a, b, c = map(int, input().split())
if (a <= b and b <= c) or (b <= a and a <= c):
    print(a + b)
elif (b <= c and c <= a) or (c <= b and b <= a):
    print(b + c)
else:
    print(a + c)