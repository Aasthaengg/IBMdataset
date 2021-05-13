import numpy as np

def main(n,k,a):
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
  print(dp[n-1])

def cc_export():
    from numba.pycc import CC
    cc = CC('my_module')
    cc.export('main','(i4,i4,i4[:])')(main)
    cc.compile()

if __name__ == '__main__':
    import sys
    if sys.argv[-1] == 'ONLINE_JUDGE':
      cc_export()
    from my_module import main
    n,k=map(int,input().split())
    a=np.array(input().split(),np.int32)
    main(n,k,a)
