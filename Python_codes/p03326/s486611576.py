N, M = map(int, input().split())
S = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*3 for _ in range(M)]
ans = [0]*8

for roop in range(8):
    a, b, c = 1, 1, 1
    if roop&1 == 1:
        a = -1
    if (roop>>1)&1 == 1:
        b = -1
    if (roop>>2)&1 == 1:
        c = -1
    dp = [[-a*10**20, -b*10**20, -c*10**20] for _ in range(M+1)]
    dp[0][0] = 0
    dp[0][1] = 0
    dp[0][2] = 0
    for i in range(N):
        for j in range(min(i, M-1), -1, -1):
            if a*(dp[j][0]+S[i][0])+b*(dp[j][1]+S[i][1])+c*(dp[j][2]+S[i][2]) > a*dp[j+1][0]+b*dp[j+1][1]+c*dp[j+1][2]:
                dp[j+1][0] = dp[j][0] + S[i][0]
                dp[j+1][1] = dp[j][1] + S[i][1]
                dp[j+1][2] = dp[j][2] + S[i][2]
    ans[roop] = a*dp[M][0]+b*dp[M][1]+c*dp[M][2]

print(max(ans))