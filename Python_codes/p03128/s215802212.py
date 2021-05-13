N, M = map(int, input().split())
A = list(map(int, input().split()))
num = [2, 5, 5, 4, 5, 6, 3, 7, 6]
dp = {0: 0}
for i in range(1, N + 1):
    dp[i] = -float('inf')
    for j in range(8, -1, -1):
        if j + 1 in A and i - num[j] >= 0:
            dp[i] = max(dp[i], dp[i - num[j]] + 1)

ans = []
while N > 0:
    for j in range(8, -1, -1):
        if j + 1 in A and N - num[j] in dp and dp[N - num[j]] == dp[N] - 1:
            ans.append(j + 1)
            N -= num[j]
            break

print(*ans, sep='')