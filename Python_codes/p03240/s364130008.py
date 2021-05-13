import sys

N = int(input())
XYH = [list(map(int, input().split())) for _ in range(N)]

# 仮の高さを計算する
for x, y, h in XYH:
    if h != 0:
        px, py, ph = x, y, h
        break

for cx in range(0, 101):
    for cy in range(0, 101):
        # 仮の高さ
        H = ph + abs(cx - px) + abs(cy - py)

        for x, y, h in XYH:
            if max(H - abs(x - cx) - abs(y - cy), 0) != h:
                break
        else:
            print(cx, cy, H)
            sys.exit()
