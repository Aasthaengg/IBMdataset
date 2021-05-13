a, b, c = [int(i) for i in input().split(" ")]

if b >= c:
    print(b + c)
else:
    s = b * 2
    c -= b
    b = 0
    if a + 1 <= c:
        s += a + 1
    else:
        s += c
    print(s)