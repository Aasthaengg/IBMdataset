from sys import stdin
def input():
    return stdin.readline().strip()

n, weight = map(int, input().split())
w, v = [0]*n, [0]*n
for i in range(n):
    w[i], v[i] = map(int, input().split())

base = w[0]

for i in range(n):
    w[i] -= base

# dp[i][j] = i個選んで重さの余りがjの時の、価値の最大値
dp = [[0] * (3*n+1) for _ in range(n+1)]

for i in range(n):
    for j in range(i, -1, -1):
        for k in range(3*j+1):
            if dp[j+1][k+w[i]] < dp[j][k] + v[i]:
                dp[j+1][k+w[i]] = dp[j][k] + v[i]

ans = 0
for i in range(n+1):
    for j in range(3*n+1):
        if base * i + j <= weight and ans < dp[i][j]:
            ans = dp[i][j]

print(ans)