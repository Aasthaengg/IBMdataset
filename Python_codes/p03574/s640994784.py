def resolve():
    H, W = [int(i) for i in input().split()]
    S = [list(input()) for _ in range(H)]
    for y in range(H):
        for x in range(W):
            if S[y][x] == ".":
                S[y][x] = 0
            else:
                S[y][x] = 9
    for y in range(H):
        for x in range(W):
            if S[y][x] < 9:
                continue
            if x - 1 >= 0:
                if y - 1 >= 0:
                    S[y - 1][x - 1] += 1
                S[y][x - 1] += 1
                if y + 1 < H:
                    S[y + 1][x - 1] += 1
            if y - 1 >= 0:
                S[y - 1][x] += 1
            S[y][x] += 1
            if y + 1 < H:
                S[y + 1][x] += 1
            if x + 1 < W:
                if y - 1 >= 0:
                    S[y - 1][x + 1] += 1
                S[y][x + 1] += 1
                if y + 1 < H:
                    S[y + 1][x + 1] += 1
    for y in range(H):
        for x in range(W):
            if S[y][x] < 9:
                S[y][x] = str(S[y][x])
            else:
                S[y][x] = "#"
        print("".join(S[y]))


resolve()
