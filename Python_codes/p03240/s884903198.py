n = int(input())
XYH = [tuple(map(int, input().split())) for _ in range(n)]
for cx in range(101):
    for cy in range(101):
        H = set()
        for x, y, h in XYH:
            if h == 0:
                continue
            H.add(h + abs(x - cx) + abs(y - cy))
        if len(H) != 1:
            continue
        H = list(H)[0]
        flag = True
        for x, y, h in XYH:
            if h != max(H - abs(x - cx) - abs(y - cy), 0):
                flag = False
                break
        if flag:
            print(cx, cy, H)
