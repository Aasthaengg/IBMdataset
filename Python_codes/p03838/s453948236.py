x, y = map(int, input().split())
ans = 0

if (x >= 0 and y > 0 and x < y) or (x < 0 and y <= 0 and x < y):
    print(y - x)
elif (x > 0 and y > 0 and x > y) or (x < 0 and y < 0 and x > y):
    print(x - y + 2)
else:
    print(abs(x + y) + 1)