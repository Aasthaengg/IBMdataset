n = int(input())
A = [0 for i in range(n)]
B = [0 for i in range(n)]
C = [0 for i in range(n)]
for i in range(n):
    A[i], B[i], C[i] = map(int, input().split())

DP = [[0 for j in range(3)] for i in range(n)]
DP[0][0], DP[0][1], DP[0][2] = A[0], B[0], C[0]
for i in range(1, n):
    DP[i][0] = max(DP[i - 1][1] + A[i], DP[i - 1][2] + A[i])
    DP[i][1] = max(DP[i - 1][0] + B[i], DP[i - 1][2] + B[i])
    DP[i][2] = max(DP[i - 1][0] + C[i], DP[i - 1][1] + C[i])

print(max(DP[n - 1][0], DP[n - 1][1], DP[n - 1][2]))