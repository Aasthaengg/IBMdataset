H,W = map(int, input().split())
s = []
for i in range(H):
    s.append(list(input()))
can_paint_all = True
for i in range(H):
    for j in range(W):
        if s[i][j] == '.':
            continue
        if 0 <= i - 1 and s[i-1][j] == '#':
            continue
        if i + 1 < H and s[i+1][j] == '#':
            continue
        if 0 <= j - 1 and s[i][j-1] == '#':
            continue
        if j + 1 < W and s[i][j+1] == '#':
            continue
        can_paint_all = False
        break
    if not can_paint_all:
        break

if can_paint_all:
    print("Yes")
else:
    print("No")