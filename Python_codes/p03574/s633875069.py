H, W = map(int, input().split())
s_l = []
for _ in range(H):
    s_l.append(list(input()))

for h in range(H):
    for w in range(W):
        if s_l[h][w] == ".":
            cnt = 0
            if h != 0:
                if w != 0:
                    if s_l[h - 1][w - 1] == "#":
                        cnt += 1
                if w != W - 1:
                    if s_l[h - 1][w + 1] == "#":
                        cnt += 1
                if s_l[h - 1][w] == "#":
                    cnt += 1
            if h != H - 1:
                if w != 0:
                    if s_l[h + 1][w - 1] == "#":
                        cnt += 1
                if w != W - 1:
                    if s_l[h + 1][w + 1] == "#":
                        cnt += 1
                if s_l[h + 1][w] == "#":
                    cnt += 1
            if w != 0:
                if s_l[h][w - 1] == "#":
                    cnt += 1
            if w != W - 1:
                if s_l[h][w + 1] == "#":
                    cnt += 1
            s_l[h][w] = str(cnt)

for h in range(H):
    print("".join(s_l[h]))
