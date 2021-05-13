n, a, b = map(int, input().split())

if a > b:
    print(0)
elif a < b:
    if n < 2:
        print(0)
    else:
        print((b - a) * (n - 2) + 1)
else:
    print(1)