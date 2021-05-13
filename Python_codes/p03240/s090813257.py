N = int(input())
lp = []

for i in range(N):
    p = list(map(int,input().split()))
    lp.append(p)

lp.sort(key=lambda x : x[2], reverse=True)


def check(cx,cy, lp):
    is_center = True
    ch = lp[0][2] + abs(cx - lp[0][0]) + abs(cy - lp[0][1])
    for p in lp[1:]:
        x,y,h = p
        if h:
            chp = h + abs(cx - x) + abs(cy - y)
            if ch != chp:
                is_center = False
                break
        else:
            if (ch-abs(cx - x) - abs(cy-y)) > 0:
                is_center = False
                break

    return is_center, ch


if N == 1:
    print(p)
else:
    for i in range(101):
        for j in range(101):
            is_center, h = check(i,j, lp)
            if is_center:
                print(i,j,h)
