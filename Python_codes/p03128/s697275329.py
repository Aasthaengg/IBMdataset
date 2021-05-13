N, M = map(int, input().split())
A = set(map(int, input().split()))

dp = [-1] * (N+1)
weights = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
# 0本のマッチで作れる最大の整数は０
dp[0] = 0

for i in range(N+1):
    for a in A:
        if i + weights[a] > N:
            continue
        dp[i + weights[a]] = max(dp[i + weights[a]], dp[i] * 10 + a)
print(dp[N])

