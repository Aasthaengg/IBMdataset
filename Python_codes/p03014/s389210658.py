H, W = map(int,input().split())
s = []
rc = [[[None]*W for _ in range(H)] for _ in range(2)]
for _ in range(H):
    s.append(list(input()))
for j in range(H):
    l = s[j]
    for i in range(W):
        if l[i] == "#":
            rc[0][j][i] = 0
        elif i > 0:
            rc[0][j][i] = rc[0][j][i-1] + 1
        else:
            rc[0][j][i] = 1
    for i in range(W-1, -1, -1):
        if l[i] == "#":
            continue
        elif i < W-1:
            rc[0][j][i] = max(rc[0][j][i+1], rc[0][j][i])
for i in range(W):
    for j in range(H):
        if s[j][i] == "#":
            rc[1][j][i] = 0
        elif j > 0:
            rc[1][j][i] = rc[1][j-1][i] + 1
        else:
            rc[1][j][i] = 1
    for j in range(H-1, -1, -1):
        if s[j][i] == "#":
            continue
        elif j < H-1:
            rc[1][j][i] = max(rc[1][j+1][i], rc[1][j][i])
ans = 0
for j in range(H):
    for i in range(W):
        ans = max(rc[0][j][i] + rc[1][j][i] - 1, ans)
print(ans)