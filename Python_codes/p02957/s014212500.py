a, b = map(int, input().split())

if a > b:
    if (a + b ) % 2 == 0:
        print((a + b) //2)
    else:
        print("IMPOSSIBLE")
elif a < b:
    if (a + b ) % 2 == 0:
        print((b + a) //2)
    else:
        print("IMPOSSIBLE")
