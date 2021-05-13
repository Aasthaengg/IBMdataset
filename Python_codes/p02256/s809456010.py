a, b = map(int, input().split())
x, y = max(a, b), min(a, b)

while 1:
    if x%y == 0:
        break
    x, y = y, x%y

print(y)