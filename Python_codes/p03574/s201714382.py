h, w = map(int, input().split())
mine = []
mine.append(["."] * (w + 2))
for i in range(h):
    mine.append(["."] + list(input()) + ["."])
mine.append(["."] * (w + 2))
ans = [[0] * w for i in range(h)]
for i in range(1, h + 1):
    for j in range(1, w + 1):
        if mine[i][j] == "#":
            ans[i - 1][j - 1] = "#"
        else:
            if mine[i - 1][j - 1] == "#":
                ans[i - 1][j - 1] += 1
            if mine[i - 1][j] == "#":
                ans[i - 1][j - 1] += 1
            if mine[i - 1][j + 1] == "#":
                ans[i - 1][j - 1] += 1
            if mine[i][j - 1] == "#":
                ans[i - 1][j - 1] += 1
            if mine[i][j + 1] == "#":
                ans[i - 1][j - 1] += 1
            if mine[i + 1][j - 1] == "#":
                ans[i - 1][j - 1] += 1
            if mine[i + 1][j] == "#":
                ans[i - 1][j - 1] += 1
            if mine[i + 1][j + 1] == "#":
                ans[i - 1][j - 1] += 1
for i in ans:
    print(*i, sep="")