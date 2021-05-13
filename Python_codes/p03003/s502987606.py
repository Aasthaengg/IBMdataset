n, m = map(int, input().split())
s = list(map(int, input().split()))
t = list(map(int, input().split()))

dp1 = [[0] * (m + 1) for _ in range(n + 1)] # ends with (i, j)
dp2 = [[0] * (m + 1) for _ in range(n + 1)] # cumsum

dp1[0][0] = 1
for i in range(n + 1):
    dp2[i][0] = 1
for j in range(m + 1):
    dp2[0][j] = 1

for i in range(n):
    for j in range(m):
        if s[i] == t[j]:
            dp1[i+1][j+1] = dp2[i][j]
        else:
            dp1[i+1][j+1] = 0
        dp2[i+1][j+1] = (dp1[i+1][j+1] + dp2[i][j+1] + dp2[i+1][j] - dp2[i][j]) % (10 ** 9 + 7)


print(dp2[-1][-1])
