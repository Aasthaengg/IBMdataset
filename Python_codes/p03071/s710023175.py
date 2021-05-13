a, b = list(map(int, input().split()))

if a > b:
    print(2 * a - 1)
elif a < b:
    print(2 * b - 1)
else:
    print(a + b)