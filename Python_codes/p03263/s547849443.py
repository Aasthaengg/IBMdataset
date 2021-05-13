H, W = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(H)]
ans = []
flg = False
for i in range(H):
    for k in range(W):
        if i % 2 != 0:
            k = W - 1 - k
        if i % 2 == 0:
            if k == W - 1:
                if i == H - 1:
                    continue
                next_i = i + 2
                next_k = k + 1
            else:
                next_i = i + 1
                next_k = k + 2
        else:
            if k == 0:
                if i == H - 1:
                    continue
                next_i = i + 2
                next_k = k + 1
            else:
                next_i = i + 1
                next_k = k
        if grid[i][k] % 2 == 1:
            if flg:
                flg = False
                continue
            flg = True
            ans.append((i+1,k+1,next_i,next_k))
        elif flg:
            ans.append((i+1,k+1,next_i,next_k))
print(len(ans))
for i in ans:
    print(i[0],i[1],i[2],i[3])