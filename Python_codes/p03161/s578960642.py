n, k = map(int, input().split())
h = list(map(int, input().split()))
MAXINT = 10**8
dp = [0 for _ in range(n)]

for i in range(1, n):
    cands = []
    for j in range(max(0, i-k), i):
        cands.append(dp[j] + abs(h[j]-h[i]))
    dp[i] = min(cands)

print(dp[n-1])