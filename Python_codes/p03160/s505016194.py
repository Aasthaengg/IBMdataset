import numpy as np
from sys import stdin,stdout
n=int(stdin.readline())
inf=1000000007
# arr = [int(x) for x in stdin.readline().split()] 
a = np.asarray((stdin.readline()+" 0 0").split(), dtype=np.int64)
dp=np.full((n+2),inf,dtype=np.int64)
dp[0]=0
for i in range(n):
    dp[i+1]=min(dp[i+1],dp[i]+abs(a[i+1]-a[i]))
    dp[i+2]=min(dp[i+2],dp[i]+abs(a[i+2]-a[i]))
# print(dp)
print(dp[n-1])
