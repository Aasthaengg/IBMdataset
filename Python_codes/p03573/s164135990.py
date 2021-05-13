x, y, z = map(int, input().split())
if x == y:
    print(z)
else:
    if x == z:
        print(y)
    else:
        print(x)
