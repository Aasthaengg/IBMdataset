#B問題
N = int(input())
C = [int(input()) for i in range(N)]
mod = 10**9+7
D = []

for i in range(N-1):
    if C[i] != C[i+1]:
        D.append(C[i])
D.append(C[-1])

M = len(D)
dp = [0 for i in range(M+1)]
dp[0] = 1
count = [0 for i in range(2*10**5+1)]

for i in range(1,M+1):
    dp[i] = dp[i-1]
    dp[i]+=count[D[i-1]]
    dp[i]%=mod
    count[D[i-1]]+=dp[i-1]
    count[D[i-1]]%=mod
    
print(dp[M])
    
    
