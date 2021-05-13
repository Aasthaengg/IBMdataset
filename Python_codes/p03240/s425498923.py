N = int(input())
XYH = [tuple(map(int,input().split())) for i in range(N)]

cands = []
for cx in range(101):
    for cy in range(101):
        ch = None
        for x,y,h in XYH:
            if h==0: continue
            d = abs(cx-x) + abs(cy-y)
            if ch is None:
                ch = h + d
            else:
                if h + d != ch:
                    break
        else:
            cands.append((cx,cy,ch))

for cx,cy,ch in cands:
    for x,y,h in XYH:
        d = abs(cx-x) + abs(cy-y)
        if h != max(ch - d, 0):
            break
    else:
        print(cx,cy,ch)
        exit()