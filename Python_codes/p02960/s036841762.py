S = input()
N = len(S)
dp = []
for _ in range(N+1):
    dp.append([0] * 13)
dp[0][0] = 1
p = 10**9+7

for i in range(1, N+1):
    X = S[N-i]
    if X == '?':
        for j in range(10):
            X = (j * pow(10, i-1, 13)) % 13
            for k in range(13):  # 上段の各あまりに対して、xのあまりを加える
                Y = dp[i-1][k]
                Z = (X + k) % 13  # 新たなあまり
                dp[i][Z] += Y % p

    else:
        X = int(X)
        X = (X * pow(10, i-1, 13)) % 13
        for k in range(13):  # 上段の各あまりに対して、xのあまりを加える
            Y = dp[i-1][k]
            Z = (X + k) % 13  # 新たなあまり
            dp[i][Z] += Y % p

print(dp[-1][5] % 1000000007)
