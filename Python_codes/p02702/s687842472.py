S = input()
N = len(S)

p = 2019
X = [0 for _ in range(p)]
X[0] = 1

dp = X[:]
ans = 0
for i in range(N):
    v = int(S[i])
    np = X[:]
    for k in range(p):
        x = (k * 10 + v) % p
        np[x] += dp[k]
    dp = np[:]
    ans += dp[0] - 1
print(ans)
