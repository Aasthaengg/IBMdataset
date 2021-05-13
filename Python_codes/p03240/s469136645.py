n = int(input())
info = [tuple(map(int, input().split())) for _ in range(n)]

for cx in range(101):
    for cy in range(101):
        h = -1
        for i in range(n):
            if info[i][2] != 0:
                h = info[i][2] + abs(info[i][0] - cx) + abs(info[i][1] - cy)
                break
        ok = True
        for i in range(n):
            v = max(h - abs(info[i][0] - cx) - abs(info[i][1] - cy), 0)
            ok &= v == info[i][2]
        if ok:
            print(cx, cy, h)
            exit()
