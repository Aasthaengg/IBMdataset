h, w = map(int, input().split())
s = [input() for _ in range(h)]

t = [[0 for _ in range(w)] for _ in range(h)]
for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            bombs = 0
            for k in range(i - 1, i + 2):
                for l in range(j - 1, j + 2):
                    if 0 <= k < h and 0 <= l < w:
                        if s[k][l] == "#":
                            bombs += 1
            else:
                t[i][j] = str(bombs)
        else:
            t[i][j] = "#"
else:
    for i in range(h):
        print("".join(t[i]))