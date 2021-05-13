h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            bomb = 0
            dx = [0]
            dy = [0]
            if i != 0:
                dx.append(-1)
            if i != h - 1:
                dx.append(1)
            if j != 0:
                dy.append(-1)
            if j != w - 1:
                dy.append(1)

            for di in dx:
                for dj in dy:
                    if s[i + di][j + dj] == "#":
                        bomb += 1

            s[i][j] = str(bomb)

for i in range(h):
    print("".join(s[i]))
