n = int(input())
A = []
B = []
C = []
for _ in range(n):
    a, b, c = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
dp = [[0] * n for _ in range(3)]
dp[0][0] = A[0]
dp[1][0] = B[0]
dp[2][0] = C[0]
for i in range(1, n):
    dp[0][i] = A[i] + max(dp[1][i-1], dp[2][i-1])
    dp[1][i] = B[i] + max(dp[0][i-1], dp[2][i-1])
    dp[2][i] = C[i] + max(dp[0][i-1], dp[1][i-1])
print(max(dp[0][-1], dp[1][-1], dp[2][-1]))