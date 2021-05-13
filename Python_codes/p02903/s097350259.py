H, W, A, B = map(int, input().split())
ans = [[0] * W for _ in range(H)]
row = [W-A] * H
column = [H-B] * W
for h in range(H):
    for w in range(W):
        if row[h] == 0:
            pass
        elif column[w] == 0 :
            pass
        else:
            ans[h][w] = 1
            row[h] -= 1
            column[w] -= 1

for row in ans:
    print(*row, sep="")
