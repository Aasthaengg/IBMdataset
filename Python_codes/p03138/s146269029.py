INFTY = 10**12
N,K = map(int,input().split())
A = list(map(int,input().split()))
A = [bin(A[i])[2:] for i in range(N)]
for i in range(N):
    A[i] = (40-len(A[i]))*"0"+A[i]
K = bin(K)[2:]
m = len(K)
K = (40-len(K))*"0"+K
dp = [[-INFTY for _ in range(2)] for _ in range(41)]
dp[0][0] = 0
for i in range(1,41):
    nd = int(K[i-1])
    cnt0 = 0
    cnt1 = 0
    for j in range(N):
        cnt0 += int(A[j][i-1])
        cnt1 += 1-int(A[j][i-1])
    if nd==0:
        dp[i][0] = 2*dp[i-1][0]+cnt0
    else:
        dp[i][0] = 2*dp[i-1][0]+cnt1
    f1 = 2*dp[i-1][1]+max(cnt0,cnt1)
    if nd==0:
        f0 = -INFTY
    else:
        f0 = 2*dp[i-1][0]+cnt0
    dp[i][1] = max(f1,f0)
tot = max(dp[40][0],dp[40][1])
print(tot)    