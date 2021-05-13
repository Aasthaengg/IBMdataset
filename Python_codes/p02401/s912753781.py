while True:
    a, b, c = input().split()
    a = int(a)
    c = int(c)
    if b == "?":
        break
    elif b == "-":
        d = a - c
    elif b == "+":
        d = a + c
    elif b == "*":
        d = a * c
    elif b == "/":
        d = a // c
    print(d)