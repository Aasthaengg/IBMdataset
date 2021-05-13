def input_li():
    return list(map(int, input().split()))

def input_int():
    return int(input())

N = input_int()
# dp[x][y] ... x日目にyを行った時の幸福度を格納する
dp = [[0] * 3 for _ in range(N)]
for i in range(N):
    a, b, c = input_li()
    if i == 0:
        dp[i][0] = a
        dp[i][1] = b
        dp[i][2] = c
    else:
        dp[i][0] = max(dp[i - 1][1], dp[i - 1][2]) + a
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + b
        dp[i][2] = max(dp[i - 1][0], dp[i - 1][1]) + c
print(max(dp[-1]))
