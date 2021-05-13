import sys
input = sys.stdin.readline

N, M = map(int, input().split())
xyz = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for bit in range(1 << 3):
    dp = [-float('inf')] * (M+1)
    dp[0] = 0
    for i in range(N):
        for j in range(M)[::-1]:
            if dp[j] != -float('inf'):
                score = 0
                for k in range(3):
                    score += xyz[i][k] * (-1)**((bit >> k) & 1)
                dp[j+1] = max(dp[j+1], dp[j] + score)
    ans = max(ans, dp[M])
print(ans)
