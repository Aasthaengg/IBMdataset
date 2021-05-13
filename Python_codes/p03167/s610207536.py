h, w = map(int, input().split())

mat = []
dp = []
m = 10**9+7

for i in range(h):
    mat.append(list(input()))
    dp.append(list([0]*w))

dp[0][0] = 1


for x in range(h):
    for y in range(w):

        if x != 0 or y != 0:
            if mat[x][y] == "#":
                dp[x][y] = 0

            else:
                dp[x][y] = (dp[x - 1][y] + dp[x][y - 1]) % m

print(dp[h - 1][w - 1])

