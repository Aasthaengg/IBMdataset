H, W = map(int, input().split())
S = [input() for _ in range(H)]
 
ans = [[0]*W for _ in range(H)]
 
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            ans[i][j] += 11

#入力が1列の場合
if W == 1:
    for i in range(H-1):
        if ans[i+1][0] > 10:
            ans[i][0] += 1
    for i in range(1, H):
        if ans[i-1][0] > 10:
            ans[i][0] += 1

    for i in range(H):
        if ans[i][0] > 10:
            ans[i][0] = "#"
        ans[i] = map(str, ans[i])
        ans[i] = "".join(ans[i])

    for a in ans:
        print(a)
    exit()
 
#横方向の確認
for i in range(H):
    for j in range(W - 1):
        if ans[i][j+1] > 10:
            ans[i][j] += 1
    for j in range(1, W):
        if ans[i][j-1] > 10:
            ans[i][j] += 1
 
#縦方向の確認
for j in range(1, W-1):
    for i in range(H-1):
        if ans[i+1][j-1] > 10:
            ans[i][j] += 1
        if ans[i+1][j] > 10:
            ans[i][j] += 1
        if ans[i+1][j+1] > 10:
            ans[i][j] += 1
 
    for i in range(1, H):
        if ans[i-1][j-1] > 10:
            ans[i][j] += 1
        if ans[i-1][j] > 10:
            ans[i][j] += 1
        if ans[i-1][j+1] > 10:
            ans[i][j] += 1
 
#j = 0
for i in range(H-1):
    if ans[i+1][0] > 10:
        ans[i][0] += 1
    if ans[i+1][1] > 10:
        ans[i][0] += 1
for i in range(1, H):
    if ans[i-1][0] > 10:
        ans[i][0] += 1
    if ans[i-1][1] > 10:
        ans[i][0] += 1
 
#j = W-1
for i in range(H-1):
    if ans[i+1][W-1] > 10:
        ans[i][W-1] += 1
    if ans[i+1][W-2] > 10:
        ans[i][W-1] += 1
for i in range(1, H):
    if ans[i-1][W-1] > 10:
        ans[i][W-1] += 1
    if ans[i-1][W-2] > 10:
        ans[i][W-1] += 1
 
for i in range(H):
    for j in range(W):
        if ans[i][j] > 10:
            ans[i][j] = "#"
    ans[i] = map(str, ans[i])
    ans[i] = "".join(ans[i])
 
for a in ans:
    print(a)