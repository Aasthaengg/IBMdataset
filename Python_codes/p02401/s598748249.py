while True:

    x, y, z = input().split()
    l = int(x)
    r = int(z)
    if y == '+':
        print(l + r)
    elif y == '-':
        print(l - r)
    elif y == '/':
        print(l // r)
    elif y == '*':
        print(l * r)
    else:
        break