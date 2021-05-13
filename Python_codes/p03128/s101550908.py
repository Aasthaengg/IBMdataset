import sys
sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())
A = list(map(int, input().split()))
num = [2, 5, 5, 4, 5, 6, 3, 7, 6]
INF = 10 ** 8

for i in range(9):
    if i + 1 not in A:
        num[i] = INF

dp = [-INF] * (N + 1)
dp[0] = 0

for i in range(1, N + 1):
    for j in range(9):
        k = i - num[j]
        if k >= 0:
            dp[i] = max(dp[i], dp[k] + 1)

ans = ''
rest = N
for i in range(dp[N]):
    t = 0
    for j in range(8, -1, -1):
        k = rest - num[j]
        if k >= 0:
            if dp[rest - num[j]] == dp[rest] - 1:
                t = max(t, j + 1)
    ans += str(t)
    rest -= num[t - 1]

print(int(ans))
