h, w = map(int, input().split(" "))
s = []
for i in range(h):
    s.append(str(input()))
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
ss = ["" for i in range(h)]
for i in range(h):
    for j in range(w):
        f = False
        if s[i][j] == ".":
            f = True
            continue
        for dy, dx in d:
            if 0 <= i + dy < h and 0 <= j + dx < w:
                if s[i + dy][j + dx] == "#":
                    f = True
                    break
        if not f:
            break
    if not f:
        break

if f:
    print("Yes")
else:
    print("No")
