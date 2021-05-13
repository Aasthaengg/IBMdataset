import sys
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
mod = 10**9 + 7
ans = int(0)

N, M = LI()
S = LI()
T = LI()
dp = [[0]*(M+1) for _ in range(N+1)]
sumdp = [[0]*(M+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,M+1):
        if S[i-1]==T[j-1]:
            dp[i][j] = sumdp[i-1][j-1]+1
            sumdp[i][j] = sumdp[i - 1][j] + sumdp[i][j - 1] +1
#            sumdp[i][j] = sumdp[i-1][j] + sumdp[i][j-1] - sumdp[i-1][j-1] + dp[i][j]
        #累積和の更新
        else:
            sumdp[i][j] = sumdp[i-1][j] + sumdp[i][j-1] - sumdp[i-1][j-1]
        sumdp[i][j] %=mod
#        ans += dp[i][j]
#print(dp)
#for row in dp:
#    ans+= sum(row)%mod
print((sumdp[N][M]+1)%mod)