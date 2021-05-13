H, W = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(H)]

ans = []

for i in range(H):
    for j in range(W):
        if a[i][j] % 2 == 1:
            if j < W-1:
                a[i][j+1] += 1
                a[i][j] -= 1
                ans.append((i, j, i, j+1))
            elif i < H-1:
                a[i+1][j] += 1
                a[i][j] -=1
                ans.append((i, j, i+1, j))  

print(len(ans))
for i, j, ni, nj in ans:
    print(i+1, j+1 , ni+1, nj+1)