w, h, n = map(int, input().split())
a = [[0], [w], [0], [h]]
for _ in range(n):
    x, y, z = map(int, input().split())
    if z == 1 or z == 2:
        a[z-1].append(x)
    else:
        a[z-1].append(y)

dx = min(a[1]) - max(a[0])
dy = min(a[3]) - max(a[2])

if dx <= 0 or dy <= 0:
    print(0)
else:
    print(dx * dy)