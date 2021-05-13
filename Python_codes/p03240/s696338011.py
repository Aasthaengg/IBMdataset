n = int(input())
z = [[0] * 101 for _ in range(101)]
xyh = [tuple(map(int, input().split())) for _ in range(n)]
xyh = sorted(xyh, key=lambda x: x[2], reverse=True)

for xi in range(101):
    for yi in range(101):
        hi = 0
        allok = True
        for i in range(n):
            x,y,h = xyh[i]
            if i == 0:
                hi = abs(xi - x) + abs(yi - y) + h
            if max(hi - abs(xi - x) - abs(yi - y), 0) != h:
                allok = False
        if allok:
            print(xi, yi, hi)
            exit()

