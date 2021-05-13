H, W = map(int,input().split())
a = []
for _ in range(H):
    l = list(map(int,input().split()))
    a.append(l)
cnt = 0
ope = []
for i in range(H):
    for j in range(W):
        if a[i][j] % 2 != 0:
            cnt += 1
            ni,nj = i+1,j
            if ni < H and nj < W and a[ni][nj] % 2 != 0:
                a[i][j] -= 1
                a[ni][nj] += 1
                ope.append((i,j,ni,nj))
                continue
            ni,nj = i,j+1
            if ni < H and nj < W and a[ni][nj] % 2 != 0:
                a[i][j] -= 1
                a[ni][nj] += 1
                ope.append((i,j,ni,nj))
                continue
            ni,nj = i+1,j
            if ni < H and nj < W:
                a[i][j] -= 1
                a[ni][nj] += 1
                ope.append((i,j,ni,nj))
                continue
            ni,nj = i,j+1
            if ni < H and nj < W:
                a[i][j] -= 1
                a[ni][nj] += 1
                ope.append((i,j,ni,nj))
                continue
            cnt -= 1
print(cnt)
for x in ope:
    print(*map(lambda y:y+1, x))