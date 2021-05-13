n = int(input())
xyh = [list(map(int, input().split())) for _ in range(n)]

xyh.sort(key=lambda x:x[2], reverse=True)
for cx in range(101):
    for cy in range(101):
        x, y, h = xyh[0]
        H = abs(x - cx) + abs(y - cy) + h
        f = True

        for i in range(1, n):
            x, y, h = xyh[i]
            h2 = max(0, H - abs(x - cx) - abs(y - cy))
            if h != h2:
                f = False
                break

        if f:
            ans = (cx, cy, H)

print(ans[0], ans[1], ans[2])
