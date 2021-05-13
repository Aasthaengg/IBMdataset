n = int(input())
exprs = []

for _ in range(n):
    exprs.append([int(i) for i in input().split()])

exprs = sorted(exprs, key=lambda x: -x[2])

for cx in range(0, 101):
    for cy in range(0, 101):
        x0, y0, h0 = exprs[0]
        ch = h0 + abs(x0 - cx) + abs(y0 - cy)
        for x, y, h in exprs[1:]:
            if h != max(ch - abs(x - cx) - abs(y - cy), 0):
                break
        else:
            print(cx, cy, ch)
            quit()
