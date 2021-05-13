w, h, n = map(int, input().split())

min_x, min_y, max_x, max_y = 0, 0, w, h
for _ in range(n):
    x, y, a = map(int, input().split())

    if a == 1:
        min_x = max(min_x, x)
    elif a == 2:
        max_x = min(max_x, x)
    elif a == 3:
        min_y = max(min_y, y)
    else:
        max_y = min(max_y, y)

if min_x < max_x and min_y < max_y:
    print((max_x - min_x) * (max_y - min_y))
else:
    print(0)