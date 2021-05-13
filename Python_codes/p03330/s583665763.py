N, C = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(C)]
grid = [list(map(int, input().split())) for _ in range(N)]
grid1 = []
grid2 = []
grid3 = []
ans = float('inf')
for i in range(N):
    for k in range(N):
        tmp = grid[i][k]
        tmp2 = i + k
        if tmp2 % 3 == 1:
            grid1.append(tmp)
        elif tmp2 % 3 == 2:
            grid2.append(tmp)
        else:
            grid3.append(tmp)
sum1 = sum(grid1)
sum2 = sum(grid2)
sum3 = sum(grid3)
tmp1 = [sum1]*C
tmp2 = [sum2]*C
tmp3 = [sum3]*C
for i in range(C):
    for k in grid1:
        tmp1[i] = tmp1[i] - k + D[k-1][i]
for i in range(C):
    for k in grid2:
        tmp2[i] = tmp2[i] - k + D[k-1][i]
for i in range(C):
    for k in grid3:
        tmp3[i] = tmp3[i] - k + D[k-1][i]
for i in range(C):
    for k in range(C):
        if i == k:
            continue
        for l in range(C):
            if i == l or k == l:
                continue
            ans = min(ans,tmp1[i]+tmp2[k]+tmp3[l])
print(ans)