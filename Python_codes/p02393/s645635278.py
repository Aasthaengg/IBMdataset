a, b, c = [int(i) for i in input().split()]
if a < b:
    if b < c:
        print(a, b, c)
    elif c < a:
        print(c, a, b)
    else:
        print(a, c, b)
else:
    if a < c:
        print(b, a, c)
    elif c < b:
        print(c, b, a)
    else:
        print(b, c, a)