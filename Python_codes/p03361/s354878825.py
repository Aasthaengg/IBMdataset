h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
f = True
for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
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
            ff = False
            for x in dx:
                for y in dy:
                    if abs(x) == abs(y):
                        continue
                    ff |= (s[i + x][j + y] == "#")
            f &= ff

print("Yes" if f else "No")
