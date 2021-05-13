n, a, b = map(int, input().split())

if 0 < n < 2 and a != b:
    print(0)
elif a > b:
    print(0)
else:
    print((n - 2) * (b - a) + 1)
