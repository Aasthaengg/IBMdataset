S = input()
N = len(S)

dp = [[0 for _ in range(13)] for _ in range(N+1)]
dp[0][0] = 1
MOD = 10**9 + 7
mul = 1
# n桁目の?は10^nを13で割った余り(mul)と掛け合わせて足される

for i in range(N):
    for k in range(10):
        if S[-i-1] != '?' and S[-i-1] != str(k):
            continue
        for j in range(13):
            dp[i+1][(j + mul * k) % 13] += dp[i][j]
    mul = (mul * 10) % 13
    for j in range(13):
        dp[i+1][j] %= MOD

res = dp[N][5]
print(res)
