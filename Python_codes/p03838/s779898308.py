x, y = map(int, input().split())

d = abs(abs(y) - abs(x))

if (x > 0 and y < 0) or (x < 0 and y > 0):
    d += 1
elif x > y:
    if x == 0 or y == 0:
        d += 1
    else:
        d += 2

print(d)
