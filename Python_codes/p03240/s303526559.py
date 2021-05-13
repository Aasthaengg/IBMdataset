N = int(input())
data = [tuple(map(int, input().split())) for _ in range(N)]
data.sort(key=lambda x: -x[2])
for cx in range(101):
    for cy in range(101):
        h0 = None
        for x, y, h in data:
            if h:
                h_tmp = h + abs(cx - x) + abs(cy - y)
                if h_tmp != h0 and h0 is not None:
                    break
                h0 = h_tmp
            else:
                if abs(cx - x) + abs(cy - y) < h0:
                    break
        else:
            print(cx, cy, h0)
            exit()
