
import sys
input = sys.stdin.buffer.readline
H, N = map(int, input().split())

INF = 1 << 40
dp = [INF]*(H+1)
dp[H] = 0
for i in range(N):
    a, b = map(int, input().split())
    for j in range(H, -1, -1):
        x = max(0, j-a)
        dp[x] = min(dp[x], dp[j]+b)

print(dp[0])
