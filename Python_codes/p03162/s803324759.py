import numpy as np

N = int(input())
a = np.array([list(map(int,input().split())) for _ in range(N)])
dp=np.zeros([N+1,3])

for i in range(1,N+1):
    for j in range(3):
        dp[i][j] = a[i-1][j]+np.maximum(dp[i-1][(1+j)%3],dp[i-1][(2+j)%3])
print(int(max(dp[N])))
