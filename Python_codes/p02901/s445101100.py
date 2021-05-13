import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = [0]*M
B = [0]*M
C = [0]*M
for i in range(M):
    A[i], B[i] = map(int, input().split())
    for c in [int(i) for i in input().split()]:
        C[i] |= 1 << (c - 1)

dp = [[float("inf")] * 2 ** N for _ in range(2)]
dp[0][0] = 0
for i, c in enumerate(C):
    for bit in range(2 ** N):
        dp[1][bit] = min(dp[1][bit], dp[0][bit])
        dp[1][c | bit] = min(dp[0][bit] + A[i], dp[1][c | bit])
    dp[0], dp[1] = dp[1], dp[0]
print(dp[0][-1] if dp[0][-1] < float("inf") else - 1)