w, h, n = map(int, input().split())
area = [0, 0, w, h]
for i in range(n):
    x, y, a = map(int, input().split())
    if a == 1 and x > area[0]:
        area[0] = x
    elif a == 2 and x < area[2]:
        area[2] = x
    elif a == 3 and y > area[1]:
        area[1] = y
    elif a == 4 and y < area[3]:
        area[3] = y
print((area[2]-area[0]) * (area[3] - area[1]) if (area[2]-area[0]) > 0 and (area[3] - area[1]) > 0 else 0)