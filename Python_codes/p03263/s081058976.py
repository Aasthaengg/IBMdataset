H, W = map(int, input().split())
D = []
res = []
for _ in range(H):
    D.append(list(map(int, input().split())))
for i in range(H-1):
    for j in range(W):
        if D[i][j]%2:
            D[i+1][j] += 1
            res.append((i+1,j+1,i+2,j+1))
for j in range(W-1):
    if D[H-1][j]%2:
        D[H-1][j+1] += 1
        res.append((H,j+1, H, j+2))
print(len(res))
for i,j,k,l in res:
    print(i,j,k,l)