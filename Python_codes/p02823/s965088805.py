n, a, b = list(map(int, input().split(" ")))

if (a + b) % 2 == 0:
    print((b - a) // 2)
    exit()
else:
    if b - 1 < n - a:
        print(b - 1 - ((b - a) // 2))
    else:
        print(n - a - ((b - a) // 2))