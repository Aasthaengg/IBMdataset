a, b = map(int, input().split())
if b==1:
    print(0)
else:
    if b >= a:
        if (b - a) % (a - 1) == 0:
            print((b - a) // (a - 1) + 1)
        else:
            print((b - a) // (a - 1) + 1 + 1)
    else:
        print(1)