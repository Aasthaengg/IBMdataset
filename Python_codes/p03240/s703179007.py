n = int(input())

xyh = [list(map(int, input().split())) for i in range(n)]
if xyh[0][2]:
    x,y,h = xyh[0]
if xyh[1][2]:
    x,y,h = xyh[1]
if xyh[-1][2]:
    x,y,h = xyh[-1]
for i in range(101):
    for j in range(101):
        k = h + abs(i - x) + abs(j - y)
        if all(h == max(k - abs(i - x) - abs(j - y), 0) for x, y, h in xyh):
            print(i, j, k)