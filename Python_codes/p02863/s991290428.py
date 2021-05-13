N, T = map(int, input().split())
AB= []
for _ in range(N):
    a, b = map(int, input().split())
    AB.append((a, b))
AB.sort(key=lambda x: x[1], reverse=True)
AB.sort()
# print(AB)
A = [x[0] for x in AB]
B = [x[1] for x in AB]

dp = [[0] * (T + 3) for _ in range(N + 3)]
dp[0][0] = 0
for i in range(N):
    for j in range(T):
        if A[i] <= j:
            dp[i + 1][j] = max(dp[i][j], dp[i][j - A[i]] + B[i])
        else:
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])

# print(dp)
ans = 0
for i in range(N):
    # print(dp[i][T - 1])
    ans = max(ans, dp[i][T - 1] + B[i])
print(ans)