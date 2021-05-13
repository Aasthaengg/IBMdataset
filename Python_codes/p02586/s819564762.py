R, C, K = map(int,input().split())
MAP = [[0 for i in range(C)] for j in range(R)]
DP = [[[0 for i in range(C+1)] for j in range(4)] for k in range(R+1)]
 
for _ in range(K):
    r, c, v = map(int,input().split())
    MAP[r-1][c-1] = v
 
for i in range(R):
    for j in range(4):
        for k in range(C):
            DP[i+1][j][k+1] = max(DP[i][3][k+1], DP[i+1][j][k])
            if j == 0:
                continue
            v = MAP[i][k]
            if v == 0:
                continue
            DP[i+1][j][k+1] = max(DP[i+1][j][k+1], max(DP[i][3][k+1], DP[i+1][j-1][k]) + v)

print(DP[R][3][C])
