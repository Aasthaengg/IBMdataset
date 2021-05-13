H, W = 82, 49
half_h = H // 2

WH = 0
BK = 1

nw, nb = map(int, input().split())
nw -= 1
nb -= 1

ret = []
for _ in range(half_h):
    ret.append([WH] * W)
for _ in range(half_h):
    ret.append([BK] * W)


def put(color, cnt, r1, r2):
    if cnt == 0:  # 追加
        return
    for r in range(r1 + 1, r2 - 1, 2):
        for c in range(0, W, 2):
            ret[r][c] = color
            cnt -= 1
            if cnt == 0:
                return


put(BK, nb, 0, half_h)
put(WH, nw, half_h, H)

print(H, W)  # 追加
for row in ret:
    print(*('#' if c == BK else '.' for c in row), sep='')
