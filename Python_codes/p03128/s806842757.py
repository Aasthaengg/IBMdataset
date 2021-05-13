N, M = map(int, input().split())
A = list(map(int, input().split()))
m = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
l = min([m[a] for a in A])
dp = [0] * (N + 1)

for i in range(N):
    for a in A:
        if (i > 0) and dp[i] == 0:
            break
        if (i + m[a] <= N):
            dp[i + m[a]] = max(dp[i + m[a]], dp[i] * 10 + a)
print(dp[-1])