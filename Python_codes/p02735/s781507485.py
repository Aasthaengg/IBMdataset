# https://atcoder.jp/contests/agc043/tasks/agc043_a
h, w = map(int, input().split())
matrix = []
for _ in range(h):
    row = list(input())
    matrix.append(row)

dp = [[float('inf')] * w for _ in range(h)]
dp[0][0] = 0
if matrix[0][0] == '#':
    dp[0][0] += 1

for i in range(h):
    for j in range(w):
        if i + 1 < h:
            if matrix[i][j] == matrix[i + 1][j]:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
            else:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
        if j + 1 < w:
            if matrix[i][j] == matrix[i][j + 1]:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j])
            else:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)

ans = (dp[-1][-1] + 1) // 2
print(ans)