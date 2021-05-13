S = input()
N = len(S)
mod = 10**9+7
P = 13
 
dp = [[0 for _ in range(P)] for _ in range(N)]
 
# 1桁目だけ事前計算
if S[N-1] == '?':
    tmp = [0 for _ in range(P)]
    for i in range(10):
        tmp[i % P] = 1
    dp[0] = tmp
else:
    dp[0][int(S[N-1]) % P] = 1
 
for i in range(1, N):
    k = N-i-1
    if S[k] == '?':
        base = pow(10, i, P)
        for j in range(10):
            r = base*j % P
            for m in range(P):
                dp[i][(m+r)%P] = (dp[i][(m+r)%P] + dp[i-1][m]) % mod
    else:
        r = pow(10, i, P) * int(S[k]) % P
        for j in range(P):
            dp[i][(j+r)%P] = max(dp[i][(j+r)%P], dp[i-1][j])
 
print(dp[-1][5])
