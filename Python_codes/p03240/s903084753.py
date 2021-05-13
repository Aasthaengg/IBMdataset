n = int(input())
xyh = []
for i in range(n):
    x, y, h = map(int, input().split())
    xyh.append((x, y, h))

for x in range(101):
    for y in range(101):
        hmax = 0
        for item in xyh:
            if item[2] > 0:
                hmax = item[2] + abs(x - item[0]) + abs(y - item[1])
                break
        is_ok = True
        for item in xyh:
            if max(0, hmax - abs(x - item[0]) - abs(y - item[1])) != item[2]:
                is_ok = False
        if is_ok:
            print(x, y, hmax)
            exit()
