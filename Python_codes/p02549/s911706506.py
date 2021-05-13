N, K = map(int, input().split())
mod = 998244353
L = [list(map(int, input().split())) for _ in range(K)]
D = {1: -1}
dp = [0 for _ in range(N)]
dp[0] = 1
for i in range(K):
    if L[i][0] in D:
        D[L[i][0]] -= 1
    else:
        D[L[i][0]] = -1
    if L[i][1]+1 in D:
        D[L[i][1]+1] += 1
    else:
        D[L[i][1]+1] = 1
dp[1] = -D[1] - 1
for i in range(2, N):
    for j in D:
        if i >= j:
            dp[i] += (-D[j]) * dp[i-j]
            dp[i] %= mod
print(dp[N-1])