a, b, x = map(int, input().split())
if a == 0:
    print(str(b // x + 1))
else:
    if a % x == 0:
        print(str(b // x - a // x + 1))
    else:
        print(str(b//x - a//x))
