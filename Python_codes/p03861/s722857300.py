def resolve():
    a, b, x = map(int, input().split())
    if a != 0:
        print(b//x-(a-1)//x)
    elif b != 0:
        print(b//x+1)
    else:
        print("1")
resolve()