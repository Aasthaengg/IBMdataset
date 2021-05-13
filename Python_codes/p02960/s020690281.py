S = list(input())
k = 0
N = len(S)
mod = 10**9+7

for i in range(N):
    if S[i] == "0":
        k += 1
    else:
        break

dp = [ [0]*13 for _ in range(N+1)]
dp[k][0] = 1

for i in range(k+1,N+1):
    for j in range(13):
        for l in range(10):
            if S[i-1] == "?" or S[i-1] == str(l):
                dp[i][(j*10+l)%13] += dp[i-1][j]
                dp[i][(j*10+l)%13] = dp[i][(j*10+l)%13] % mod
print(dp[N][5])