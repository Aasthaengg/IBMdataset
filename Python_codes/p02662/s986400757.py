N,S = list(map(int,input().split()))
A = list(map(int,input().split()))
dp = [[0]*(N+1) for i in range(S+1)]
p = 998244353

twos = [1]*N
for i in range(1,N):
    twos[i] = (twos[i-1]*2)%p

for j in range(1,N+1):
    flag = 0
    for i in range(1,S+1):
        if flag==0:
            dp[i][j] = (dp[i][j-1]*2)%p
        else:
            dp[i][j] = (dp[i][j-1]*2+dp[i-A[j-1]][j-1])%p
        if i==A[j-1]:
            dp[i][j] += twos[j-1]
            flag = 1
print(dp[-1][-1]%p)