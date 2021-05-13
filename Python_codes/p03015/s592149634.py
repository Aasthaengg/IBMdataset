mod = 10 ** 9 + 7

S = input()
N = len(S)

dp = [[0] * 2 for _ in range(N + 10)]
dp[0][0] = 1

for i in range(N):
    nd = int(S[i])
    for k in range(2):
        for a in range(2):
            for b in range(2):
                ni = i + 1
                nk = k
                if a == b == 1:
                    continue
                if nk == 0:
                    if nd == 1 and a + b == 0:
                        nk += 1
                    if nd == 0 and a + b == 1:
                        continue
                dp[ni][nk] += dp[i][k]
                dp[ni][nk] %= mod

ans = (dp[N][0] + dp[N][1]) % mod
print(ans)