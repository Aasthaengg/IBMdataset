def resolve():
    x, y = input().split()
    nx = ord(x)
    ny = ord(y)
    if nx < ny:
        print("<")
    elif nx > ny:
        print(">")
    else:
        print("=")
resolve()