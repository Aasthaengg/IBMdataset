N, K = map(int, input().split())

MOD = 998244353

L_list = []
R_list = []
for i in range(K):
    L, R = map(int, input().split())
    L_list.append(L)
    R_list.append(R)

dp = [0] * (N+1)
dp[0] = 0
dp[1] = 1
sdp = [0] * (N+1)
sdp[0] = 0
sdp[1] = 1


for i in range(2, N+1):
    for j in range(len(L_list)):
        if i - R_list[j]-1 < 0:
            R_pos = 0
        else:
            R_pos = i - R_list[j] - 1
        dp[i] += (sdp[i - L_list[j]] - sdp[R_pos])%MOD
        dp[i] %= MOD
    sdp[i] = sdp[i-1] + dp[i]
    sdp[i] %= MOD
    #print(dp)
    #print("s", sdp)
print(dp[N])