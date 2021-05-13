a, b, c, d = map(int, input().split())
while True:
    if (c - b) <= 0:
        print("Yes")
        exit()
    else:
        c = c - b
        if a - d <= 0:
            print("No")
            exit()
        else:
            a = a - d

