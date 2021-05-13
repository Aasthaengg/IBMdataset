import sys
input = sys.stdin.readline

N, Ma, Mb = map(int, input().split())
MAX = 400
INF = float('inf')
dp = [[INF] * (MAX+1) for _ in range(MAX+1)]
dp[0][0] = 0
for _ in range(N):
    a, b, c = map(int, input().split())
    for i in range(a, MAX+1)[::-1]:
        for j in range(b, MAX+1)[::-1]:
            dp[i][j] = min(dp[i][j], dp[i-a][j-b] + c)
ans = INF
x = 1
while Ma*x <= MAX and Mb*x <= MAX:
    ans = min(ans, dp[Ma*x][Mb*x])
    x += 1
print(ans if ans < INF else -1)