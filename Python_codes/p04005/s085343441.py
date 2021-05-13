a, b, c = map(int, input().split())
if a * b * c % 2:
    print(min(a * b, b * c, c * a))
else:
    print(0)