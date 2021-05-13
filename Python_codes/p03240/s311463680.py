n = int(input())
xyh = []
for i in range(n):
    x, y, h = [int(i) for i in input().split()]
    xyh.append((x, y, h))

xyh.sort(key=lambda x: x[2], reverse=True)

for i in range(101):
    for j in range(101):
        x, y, h = xyh[0]
        H = h + abs(i - x) + abs(j - y)
        for x, y, h in xyh[1:]:
            if h != max(H - abs(i - x) - abs(j - y), 0):
                break
        else:
            ans = i, j, H
print(*ans)
