import numpy as np
import sys
input = sys.stdin.readline
[N,K]=[int(x) for x in input().split()]
h=[int(x) for x in input().split()]
h=np.array(h)
dp=np.zeros(N,dtype=int)
 
for i in range(1,N):
  last=min(K,i)+N-i
  dp[N-i-1]=min(dp[N-i:last]+np.abs(h[N-i:last]-h[N-i-1]))
print(dp[0])