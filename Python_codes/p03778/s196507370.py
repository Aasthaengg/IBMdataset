W, a, b = map(int, input().split())

A = a + W
if b > a:
    if b - A <= 0:
        print(0)
    else:
        print(b - A)
else:
    B = b + W
    if a - B <= 0:
        print(0)
    else:
        print(a-B)
