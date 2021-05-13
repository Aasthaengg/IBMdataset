n, a, b = map(int, input().split())
x = a * n - a + b
y = b * n - b + a


if a > b:
    print(0)
elif a == b and n == 1:
    print(1)
elif a != b and n == 1:
    print(0)
else:
    print(y - x + 1)
