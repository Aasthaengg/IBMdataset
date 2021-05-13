n = int(input())
xyh = [list(map(int, input().split())) for _ in range(n)]
xyh.sort(key=lambda x: x[2], reverse=True)

def esth(x, y, h, cx, cy):
    return h + abs(x-cx) + abs(y-cy)


for cx in range(101):
    for cy in range(101):
        f = True
        ch = 0
        for x, y, h in xyh:
            if ch == 0 and h > 0:
                ch = esth(x, y, h, cx, cy)
            elif h > 0:
                if ch != esth(x, y, h, cx, cy):
                    f = False
                    break
            else:
                if max(ch - abs(x-cx) - abs(y-cy), 0) != h:
                    f = False
                    break
        if f:
            print('{} {} {}'.format(cx, cy, ch))
            break