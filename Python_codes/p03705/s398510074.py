n, a, b = map(int, input().split())

if (n == 1) or (a > b):
    print(1 if a == b else 0)
else:
    small, large = a * (n - 2), b * (n - 2)
    print(large - small + 1)