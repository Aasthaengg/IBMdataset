n = int(input())
xyh = [list(map(int,input().split())) for i in range(n)]
xyh = sorted(xyh, key=lambda x:(x[2]), reverse=True)

ans = -1, -1, -1
for cx in range(101):
    for cy in range(101):
        flg = True
        x, y, h = xyh[0][0], xyh[0][1], xyh[0][2]
        ch = abs(cx-x) + abs(cy-y) + h
        for i in range(1,n):
            x, y, h = xyh[i][0], xyh[i][1], xyh[i][2]
            tmph = max(ch - abs(cx-x) - abs(cy-y), 0)
            if h != tmph:
                flg = False
                break
        if flg:
            ans = cx, cy, ch
print(*ans)