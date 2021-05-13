H,W = map(int, input().split())
fs = []
for i in range(H):
    fs.append(input())

lefts = [[0]*W for i in range(H)]
rights = [[0]*W for i in range(H)]
for i in range(H):
    for j in range(W):
        if fs[i][j] == "#":
            lefts[i][j] = 0
        if fs[i][j] == ".":
            if j == 0:
                lefts[i][j] = 1
            else:
                lefts[i][j] = lefts[i][j-1] + 1
        jr = W - j - 1
        if fs[i][jr] == "#":
            rights[i][jr] = 0
        else:
            if jr == W-1:
                rights[i][jr] = 1
            else:
                rights[i][jr] = rights[i][jr+1] + 1
ups = [[0]*W for i in range(H)]
downs = [[0]*W for i in range(H)]
for j in range(W):
    for i in range(H):
        if fs[i][j] == "#":
            ups[i][j] = 0
        else:
            if i == 0:
                ups[i][j] = 1
            else:
                ups[i][j] = ups[i-1][j] + 1
        ir = H - i - 1
        if fs[ir][j] == "#":
            downs[ir][j] = 0
        else:
            if ir == H-1:
                downs[ir][j] = 1
            else:
                downs[ir][j] = downs[ir+1][j] + 1


# for l in lefts:
#     print(*l)
# print("-----------")
# for r in rights:
#     print(*r)
# print("updown")
# for l in ups:
#     print(*l)
# print("-----------")
# for r in downs:
#     print(*r)

ans = 0
for i in range(H):
    for j in range(W):
        x = lefts[i][j] + rights[i][j] + ups[i][j] + downs[i][j]
        # print(i,j,lefts[i][j] ,rights[i][j] ,ups[i][j] ,downs[i][j])
        ans = max(x,ans)
print(ans-3)