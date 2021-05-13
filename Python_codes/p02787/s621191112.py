import sys

H, N = map(int, input().split())
A = [0] * N
B = [0] * N

for i in range(N):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    A[i] = a
    B[i] = b

max_A = max(A)
INF = 10**18
dp = [INF] * (H + max_A)
dp[0] = 0

for i in range(H):
    for j in range(N):
        dp[i + A[j]] = min(dp[i] + B[j], dp[i + A[j]])

print(min(dp[H:H + max_A]))
