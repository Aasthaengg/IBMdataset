n,t = map(int, input().split())
ls = [list(map(int, input().split())) for i in range(n)]
t-=1
dp1 = [[0 for _ in range(t+1)] for _ in range(n+1)]
for i in range(n+1):
    for j in range(t+1):
        if i>0 and j>=ls[i-1][0]:
                dp1[i][j] = max(dp1[i-1][j-ls[i-1][0]] + ls[i-1][1] ,dp1[i-1][j])

        elif i>0:
            dp1[i][j] = dp1[i-1][j]

dp2 = [[0 for _ in range(t+1)] for _ in range(n+1)]
for i in range(n, -1, -1):
    for j in range(t+1):
        if i<n and j>=ls[i][0]:
                dp2[i][j] = max(dp2[i+1][j-ls[i][0]] + ls[i][1] ,dp2[i+1][j])

        elif i<n:
            dp2[i][j] = dp2[i+1][j]

ans=0
for i in range(n):
    for j in range(t):
        ans = max(dp1[i][j] + dp2[i+1][t-j] + ls[i][1],ans)


print(ans)