a, b = map(int, input().split())
if a + b == 24:
    print(0)
elif a + b > 24:
    print(a + b - 24)
else:
    print(a + b)
