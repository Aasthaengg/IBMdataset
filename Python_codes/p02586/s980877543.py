r,c,k = map(int,input().split())
lst = [[0]*c for _ in range(r)]
for i in range(k):
    a,b,v = map(int,input().split())
    lst[a-1][b-1] = v
dp0 = [[0]*c for _ in range(r)]
dp1 = [[0]*c for _ in range(r)]
dp2 = [[0]*c for _ in range(r)]
dp3 = [[0]*c for _ in range(r)]
dp1[0][0] = lst[0][0]

for i in range(r):
    for j in range(c):
        s = max(dp0[i][j], dp1[i][j], dp2[i][j], dp3[i][j])
        x,y = i+1,j
        if x < r:
            dp0[x][y] = max(dp0[x][y], s)
            if lst[x][y]:
                dp1[x][y] = max(dp1[x][y], s+lst[x][y])
        x,y = i,j+1
        if y < c:
            dp3[x][y] = max(dp3[i][j], dp3[x][y])
            if lst[x][y]:
                dp3[x][y] = max(dp2[i][j]+lst[x][y], dp3[x][y])
            
            dp2[x][y] = max(dp2[x][y], dp2[i][j])
            if lst[x][y]:
                dp2[x][y] = max(dp2[x][y], dp1[i][j]+lst[x][y])
            
            dp1[x][y] = max(dp1[x][y], dp1[i][j])
            if lst[x][y]:
                dp1[x][y] = max(dp1[x][y], dp0[i][j]+lst[x][y])
            
            dp0[x][y] = max(dp0[x][y], dp0[i][j])
print(max(dp0[-1][-1], dp1[-1][-1], dp2[-1][-1], dp3[-1][-1]))
