H, W = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(H)]

# 順に見ていく
res = []
cnt = 0
for h in range(H):
    if h % 2 == 0:
        for w in range(W):
            if h == H - 1 and w == W - 1:
                continue
            elif a[h][w] % 2 == 1 and w != W - 1:
                cnt += 1
                res.append([h + 1, w + 1, h + 1,  w + 2])
                a[h][w + 1] += 1
            elif a[h][w] % 2 == 1 and w == W - 1:
                cnt += 1
                res.append([h + 1, w + 1, h + 2, w + 1])
                a[h + 1][w] += 1
            else:
                continue
    elif h % 2 == 1:
        for w in range(W-1, -1, -1):
            if h == H - 1 and w == 0:
                continue
            elif a[h][w] % 2 == 1 and w != 0:
                cnt += 1
                res.append([h + 1, w + 1, h + 1,  w])
                a[h][w - 1] += 1
            elif a[h][w] % 2 == 1 and w == 0:
                cnt += 1
                res.append([h + 1, w + 1, h + 2, w + 1])
                a[h + 1][w] += 1
            else:
                continue

print(cnt)
for v in res:
    print(*v)