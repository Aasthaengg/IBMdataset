N = int(input())
XYH = [tuple(map(int, input().split())) for _ in range(N)]
sXYH = sorted(XYH, key=lambda x:x[2], reverse=True)

for cx in range(101):
    for cy in range(101):
        x, y, h = sXYH[0]
        H = h + abs(x-cx) + abs(y-cy)
        res = []
        for x, y, h in sXYH[1:]:
            temp = (h == max(H-abs(x-cx)-abs(y-cy), 0))
            res.append(temp)
        if all(res):
            print(cx, cy, H)
            exit()
