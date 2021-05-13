N = int(input())
vac = []
for i in range(N):
    vac.append(list(map(int, input().split())))

dp = [[0 for _ in range(3)] for _ in range(N+1)]   

for i in range(N):
    for j in range(3):
        for k in range(3):
            if(j == k):
                continue
            dp[i+1][k] = max(dp[i+1][k], dp[i][j]+vac[i][k])
print(max(dp[-1]))