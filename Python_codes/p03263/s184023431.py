H, W = map(int, input().split(' '))
A = [list(map(int, input().split(' '))) for i in range(H)]
cnt = 0
ans = []
for i in range(H):
    for j in range(W):
        if A[i][j] % 2 == 0:
            continue
        tmp = ''
        flg = True
        for x, y in [[1, 0], [0, 1]]:
            if 0 <= i+x < H and 0 <= j+y < W:
                if A[i+x][j+y] % 2 != 0:
                    A[i][j] -= 1
                    cnt += 1
                    A[i+x][j+y] += 1
                    ans.append([i, j, i+x, j+y])
                    flg = False
                    break
                else:
                    tmp = [x, y]
        if flg and tmp:
            cnt += 1
            A[i+tmp[0]][j+tmp[1]] += 1
            A[i][j] -= 1
            ans.append([i, j, i+tmp[0], j+tmp[1]])
print(cnt)
for i, j, k, l in ans:
    print(i+1, j+1, k+1, l+1)
