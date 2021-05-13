import sys
input = sys.stdin.readline

N = int(input())

def li():
    return [float(x) for x in input().split()]

P = li()
# dp[i][j]: i番目のコインを投げた時に、表がj枚となる確率
dp = [[0] * (N+1) for _ in range(N)]

dp[0][1], dp[0][0] = P[0], 1 - P[0]

for i in range(1, N):
    for j in range(N+1):
        p = P[i]
        if j > 0:
            dp[i][j] = dp[i-1][j-1] * p + dp[i-1][j] * (1.0 - p)
        else:
            dp[i][0] = dp[i-1][0] * (1.0 - p)

total = 0
for j in range(N+1):
    if 2 * j > N:
        total += dp[N-1][j]

print(total)
