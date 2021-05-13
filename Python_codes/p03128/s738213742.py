N, M, *A = map(int, open(0).read().split())

match = {1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
dp = [[0] * M for _ in range(N + 1)]

for i in range(N + 1):
    for j in range(M):
        for k in range(M):
            if (i - match[A[k]] == 0) or \
                   (i - match[A[k]] > 0 and dp[i - match[A[k]]][j] != 0):
                dp[i][k] = max(dp[i][k], 
                               dp[i - match[A[k]]][j] * 10 + A[k])

print(max(dp[-1]))

