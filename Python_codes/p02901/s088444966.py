import sys
input=sys.stdin.readline
n, m = map(int, input().split())
A = [0] * m
B = [0] * m
C = [[] for _ in range(m)]
for i in range(m):
    a, b = map(int, input().split())
    A[i] = a
    B[i] = b
    c = list(map(int, input().split()))
    C[i] = c
D = [0] * m
for i in range(m):
    d = 0
    for j in C[i]:
        d |= 1 << (j - 1)
    D[i] = d
# dp[i][s], i番目までの鍵を使ってSを作る最小コスト
infi = 10 ** 20
dp = [[infi for i in range(2 ** n + 1)] for _ in range(m + 1)]
dp[0][0] = 0
for i in range(m):
    for s in range(2 ** n):
        ni = i + 1
        ns = s
        # 使わないとき
        dp[ni][ns] = min(dp[i][s], dp[ni][ns])
        # 使うとき
        ns = s | D[i]
        dp[ni][ns] = min(dp[ni][ns], dp[i][s] + A[i])
ans = dp[m][2 ** n - 1]
print(ans if ans < infi else -1)
