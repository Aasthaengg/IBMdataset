a, b, c = map(int, input().split())
total = a + b + c
if total >= c * 2 - 1:
    print(b + c)
else:
    print((a + b) * 2 + 1 - a)