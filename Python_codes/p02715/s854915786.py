import numpy as np
from numba import jit

n,k=map(int,input().split())

@jit
def main():
  mod=10**9+7
  L=np.zeros(k+1,dtype='int64')
  ans=0
  for x in range(k,0,-1):
    lx=pow((k//x),n,mod)
    cnt=1
    while x*(cnt+1)<=k:
      cnt+=1
      lx-=L[x*cnt]
    L[x]=lx%mod
    ans+=(L[x]*x)%mod
  return ans%mod

if __name__=="__main__":
  print(main())