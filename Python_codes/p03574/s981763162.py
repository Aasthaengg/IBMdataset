H, W = map(int, input().split())
XY = [[] for _ in range(H)]
for h in range(H):
    XY[h] = [s for s in input()]


for h in range(H):
    ans = ""
    for w in range(W):
        if XY[h][w] == "#":
            ans += "#"
            continue
        cnt = 0
        for h_diff in [-1, 0, 1]:
            for w_diff in [-1, 0, 1]:
                if h + h_diff < 0 or w + w_diff < 0:
                    continue
                elif h + h_diff >= H or w + w_diff >= W:
                    continue
                else:
                    if XY[h + h_diff][w + w_diff] == "#":
                        cnt += 1
        ans += str(cnt)
    print(ans)
