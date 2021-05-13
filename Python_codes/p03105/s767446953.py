a, b, c = map(int, input().split())
if b < a:
    print(0)
elif c <= b // a:
    print(c)
else:
    print(b // a)