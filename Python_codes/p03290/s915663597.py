D, G = map(int, input().split())
T = []
acc = 0
for i in range(D):
    p, c = map(int, input().split())
    acc += p
    T.append([p, c])
dp = [[0]*(acc+1) for _ in range(D+1)]
l = 0
for i in range(1, D + 1):
    for j in range(1, acc + 1):
        l += T[i-1][0]
        for k in range(T[i-1][0] + 1):
            if j <= l and j - k >= 0:
                if k == T[i-1][0]:
                    dp[i][j] = max([dp[i - 1][j - k] + 100 * i * k + T[i - 1][1], dp[i - 1][j]])
                else:
                    dp[i][j] = max([dp[i - 1][j - k] + 100 * i * k, dp[i - 1][j]])

for i in range(acc + 1):
    if dp[D][i] >= G:
        print(i)
        break