import numpy as np
from numba import njit
@njit
def main():
  # Worst Case
  #n,k=100000,100
  #a=[p for p in range(100000)]
  
  kl=[p for p in range(1,k+1)]
  dp=[10**9]*(n)
  dp[0]=0
  for i in range(n):
    for j in kl:
      ij=i+j
      if ij < n:
        m=dp[i]+abs(a[i]-a[ij])
        if m < dp[ij]:
          dp[ij]=m
  return dp[n-1]

n,k=map(int,input().split())
a=np.array(list(map(int,input().split())))
print(main())

