
N, M = map(int, input().split())
X = list(map(int, input().split()))

X.sort(reverse=True)
num = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
dp = [-1] * (N + 1)
dp[0] = 0

for a in X:
    for i in range(N + 1):
        if dp[i] == -1 or i + num[a] > N:
            continue
        dp[i + num[a]] = max(dp[i + num[a]], dp[i] * 10 + a)

print(dp[-1])
