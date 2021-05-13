a, b, c = map(int, input().split())

x = 3 * max(a, b, c) - a - b - c
if x % 2 == 0:
    print(x // 2)
else:
    print(x // 2 + 2)
