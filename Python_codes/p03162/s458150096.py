import numpy as np
N = int(input())
abc = []
for i in range(N):
  abc.append([int(i) for i in input().split()])
abc.append([0,0,0])
dp = np.zeros([N+1,3])
#print(dp)

for i in range(1,N+1):
  dp[i][0],dp[i][1],dp[i][2] = max(dp[i-1][1]+abc[i-1][0], dp[i-1][2]+abc[i-1][0]), max(dp[i-1][0]+abc[i-1][1], dp[i-1][2]+abc[i-1][1]), max(dp[i-1][1]+abc[i-1][2], dp[i-1][0]+abc[i-1][2])
  #print(dp)
print(int(max(dp[N])))
