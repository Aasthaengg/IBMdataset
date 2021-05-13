H, W, K = map(int, input().split())
s = [input() for _ in range(H)]
ans = [[0] * W for _ in range(H)]

count = 0
for i in range(H):
    count_row = 0
    for j in range(W):
        if s[i][j] == "#":
            count_row += 1
            count += 1
        ans[i][j] = max(count_row, 1) + count-count_row
    if count_row==0:
        if count != 0:
            ans[i] = ans[i-1]
    if count != 0 and count==count_row:
        for ii in range(i):
            ans[ii] = ans[i]
for an in ans:
    print(*an)