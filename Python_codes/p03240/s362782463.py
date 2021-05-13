n = int(input())
xyh = [list(map(int, input().split())) for _ in range(n)]

for x, y, h in xyh:
    if h > 0:
        x0, y0, h0 = x, y, h
        break

ans = [None] * 3
for cx in range(101):
    for cy in range(101):
        top = h0 + abs(x0 - cx) + abs(y0 - cy)
        bl = True
        for x, y, h in xyh[1:]:
            h_calc = max(top - abs(x - cx) - abs(y - cy), 0)
            if h_calc != h:
                bl = False
                break

        if bl:
            ans = [cx, cy, top]

print(*ans)
