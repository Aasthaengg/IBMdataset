def resolve():
    x, a, b = map(int, input().split())
    la = abs(x-a)
    lb = abs(x-b)

    if la < lb:
        print("A")
    elif lb < la:
        print("B")
resolve()