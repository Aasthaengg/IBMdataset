n = int(input())
xyh = [tuple(map(int, input().split())) for _ in range(n)]
xyh = sorted(xyh, key=lambda x: x[2], reverse=True)

ans = False
for cy in range(101):
    for cx in range(101):
        x0, y0, h0 = xyh[0]
        H = abs(x0-cx) + abs(y0-cy) + h0
        # 全てのクエリについて高さを計算する
        for x, y, h in xyh[1:]:
            hh = max(H-abs(x-cx)-abs(y-cy), 0)
            if h != hh:
                break
        else:
            # 回り切ったら答え
            ans = True
            print(cx, cy, H)
            break
        if ans:
            break
    if ans:
        break
