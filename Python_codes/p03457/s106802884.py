n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]

x = y = t = 0
for i in range(n):
    dx, dy, dt = l[i][1], l[i][2], l[i][0]
    dist = abs((dx - x) + (dy - y))

    if abs(dt - t) < dist:
        print("No")
        exit()
    if abs(dt - t) % 2:
        if dist % 2 == 0:
            print("No")
            exit()
    else:
        if dist % 2 == 1:
            print("No")
            exit()
    x, y, t = dx, dy, dt
print("Yes")