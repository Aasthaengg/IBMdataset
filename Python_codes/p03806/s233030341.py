import sys
readlines = sys.stdin.buffer.readlines
input = sys.stdin.buffer.readline
N, Ma, Mb = map(int, input().split())
X = [map(int, line.split()) for line in readlines()]
X = [(a*Mb-b*Ma, c) for a, b, c in X]

INF = 1 << 30
MAX = 10000
MID = MAX//2
dp = [INF]*(MAX+1)
ans = INF
for i, (x, c) in enumerate(X):
    if x == 0:
        ans = min(ans, c)
        continue

    if x > 0:
        for j in range(MAX, x-1, -1):
            dp[j] = min(dp[j], dp[j-x]+c)
    else:
        for j in range(MAX+x):
            dp[j] = min(dp[j], dp[j-x]+c)

    dp[MID+x] = min(dp[MID+x], c)

ans = min(ans, dp[MID])
print(ans if ans < INF else -1)
