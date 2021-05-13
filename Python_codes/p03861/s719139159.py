a, b, x = map(int, input().split())
if a == 1:
    print(b // x)
else:
    print(b // x - (a - 1) // x)
