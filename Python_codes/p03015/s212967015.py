N = input()
k = len(N)
mod = 10**9+7
DP = [[0,0] for i in range(k+1)]
DP[0][0] = 1
DP[0][1] = 0
for i in range(1,k+1):
    if N[i-1] == "1":
        DP[i][0] = (DP[i-1][0]*2)%mod
        DP[i][1] = (DP[i-1][1]*3+DP[i-1][0])%mod
    if N[i-1] == "0":
        DP[i][0] = DP[i-1][0]
        DP[i][1] = (DP[i-1][1]*3)%mod
print((DP[k][0]+DP[k][1])%mod)