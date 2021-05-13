from copy import deepcopy
N = int(input())
origin_dp = [list(map(int, input().split())) for _ in range(N)]
dp = deepcopy(origin_dp)

for i in range(N):
    for j in range(N):
        for k in range(N):
            dp[j][k] = min(dp[j][k], dp[j][i]+dp[i][k])
        

judge = origin_dp == dp

if judge:
    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if dp[j][k] == 0 or dp[j][i] == 0 or dp[i][k] == 0: continue

                if dp[j][k] == dp[j][i] + dp[i][k]:
                    dp[j][k] = 0
        
    for i in range(N):
        for j in range(i+1,N):
            ans += dp[i][j]

    print(ans)
else:
    print(-1)
