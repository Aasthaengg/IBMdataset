R,C,K = map(int,input().split())
dp0 = [[0 for _ in range(C+1)] for f in range(R+1)]
dp1 = [[0 for _ in range(C+1)] for f in range(R+1)]
dp2 = [[0 for _ in range(C+1)] for f in range(R+1)]
dp3 = [[0 for _ in range(C+1)] for f in range(R+1)]
vl = [[0 for _ in range(C+1)] for f in range(R+1)]

for i in range(K):
	r,c,v = map(int,input().split())
	vl[r][c] = v

for i in range(1, R+1):
	for j in range(1, C+1):
		dp0[i][j] = max(dp0[i][j], dp0[i-1][j], dp1[i-1][j], dp2[i-1][j], dp3[i-1][j])
		dp3[i][j] = max(dp3[i][j], dp3[i][j-1], dp2[i][j-1]+vl[i][j], dp2[i][j]+vl[i][j])
		dp2[i][j] = max(dp2[i][j], dp2[i][j-1], dp1[i][j-1]+vl[i][j], dp1[i][j]+vl[i][j])
		dp1[i][j] = max(dp1[i][j], dp1[i][j-1], dp0[i][j-1]+vl[i][j], dp0[i][j]+vl[i][j])

print(max(dp0[R][C], dp1[R][C], dp2[R][C], dp3[R][C]))