r,c,kk = map(int, input().split())

a = [[0 for j in range(c)] for i in range(r)]
dp1 = [[0 for j in range(c+1)] for i in range(r+1)]
dp2 = [[0 for j in range(c+1)] for i in range(r+1)]
dp3 = [[0 for j in range(c+1)] for i in range(r+1)]
dp4 = [[0 for j in range(c+1)] for i in range(r+1)]

for i in range(kk):
  b,cc,d = map(int, input().split())
  b -= 1
  cc -= 1
  a[b][cc] = d

for i in range(r):
  for j in range(c):
    dp4[i][j] = max(dp4[i][j],dp3[i][j]+a[i][j])
    dp3[i][j] = max(dp3[i][j],dp2[i][j]+a[i][j])
    dp2[i][j] = max(dp2[i][j],dp1[i][j]+a[i][j])
    dp1[i][j+1] = max(dp1[i][j+1],dp1[i][j])
    dp2[i][j+1] = max(dp2[i][j+1],dp2[i][j])
    dp3[i][j+1] = max(dp3[i][j+1],dp3[i][j])
    dp4[i][j+1] = max(dp4[i][j+1],dp4[i][j])
    dp1[i+1][j] = max(dp1[i+1][j],dp1[i][j],dp2[i][j],dp3[i][j],dp4[i][j])
ans=  0
ans = max(dp1[r-1][c-1],dp2[r-1][c-1],dp3[r-1][c-1],dp4[r-1][c-1])
print (ans)