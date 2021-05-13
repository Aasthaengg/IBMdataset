x, y = map(int, input().split())
count = abs(abs(x)-abs(y))

if x * y < 0:
    count += 1
elif x * y == 0 and x > y:
    count += 1
elif x * y > 0:
    if x < 0 and abs(x) < abs(y):
        count += 2
    elif x > 0 and abs(x) > abs(y):
        count += 2

print(count)