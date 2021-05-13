from numba import jit
import math

N, K = map(int,input().split())
h = list(map(int,input().split()))
@jit
def nya(N, K, h):
  dp=[0]*N
  for i in range(1,N):
    value=math.inf
    for j in range(1,K+1):
      if i-j<0:
        break
      value=min(value,dp[i-j]+abs(h[i]-h[i-j]))
    dp[i]=value
  return(dp[N-1])
 
print(nya(N,K,h))