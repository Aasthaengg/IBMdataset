n,m = map(int,input().split())
g = []
dp = [[float('inf')]*n for _ in range(n)]
for i in range(n):
    dp[i][i]=0
for _ in range(m):
    a,b,c = map(int,input().split())
    g.append((a-1,b-1,c))
    dp[a-1][b-1] = c
    dp[b-1][a-1] = c
for k in range(n):
    for i in range(n):
        for j in range(n):
            dp[i][j] = min(dp[i][j],dp[i][k]+dp[k][j])
# print(dp)
cnt = 0

for a,b,c in g:
    f = True
    for i in range(n):
        if dp[i][a]+c==dp[i][b]:
            f = False
            break
    if f:
        cnt += 1
print(cnt)