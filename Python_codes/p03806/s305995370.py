n, ma, mb = map(int,input().split())
A = [list(map(int,input().split())) for i in range(n)]

s = 400

DP = [[0] * (s+1) for i in range(s+1)]
C = [[float("inf")] * (s+1) for i in range(s+1)]
DP[0][0] = 1
C[0][0] = 0

for k in range(n):
    for i in range(s, -1, -1):
        for j in range(s, -1, -1):
            x = i-A[k][0]
            y = j-A[k][1]
            # print(x,y,i,j)
            if x >= 0 and y >= 0 and DP[x][y] == 1 and C[x][y] + A[k][2] < C[i][j]:
                C[i][j] = C[x][y] + A[k][2]
                DP[i][j] = 1
            # print(DP)

ans = float("inf")
ma0 = ma
mb0 = mb
while ma <= s and mb <= s:
    if DP[ma][mb] == 1:
        ans = min(ans, C[ma][mb])
    ma += ma0
    mb += mb0

if ans == float("inf"):
    print(-1)
else:
    print(ans)
