def solve():
    a, b = map(int, input().split())
    if b == 1:
        print(0)
        exit()

    x = 1
    y = a * 1
    while y < b:
        y += a - 1
        x += 1
    print(x)


solve()
