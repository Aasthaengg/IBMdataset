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
    for small in range(2):
        for d in range(2):
            ni = i
            nsmall = small
            nd = int(K[i-1])
            cnt = 0
            for j in range(N):
                cnt += int(A[j][i-1])^d
            if small==0:
                if d>nd:continue
                if d<nd:nsmall=1
            dp[ni][nsmall] = max(dp[ni][nsmall],2*dp[i-1][small]+cnt)
tot = max(dp[40][0],dp[40][1])
print(tot)    