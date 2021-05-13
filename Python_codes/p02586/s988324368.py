import sys
from numpy import*
def main(h,w,k,t):
    c=zeros((3001,3001),int_)
    dp=zeros((4,3001,3001),int_)
    for i in range(k):
        y,x,v=t[i]
        c[y,x]=v
    for i in range(1,h+1):
        for j in range(1,w+1):
            x=max(dp[:,i-1,j])
            for k in range(4):
                if k:dp[k,i,j]=max(dp[k,i,j-1],dp[k-1,i,j-1]+c[i,j])
                else:dp[k,i,j]=max(dp[k,i,j-1],x)
            dp[1,i,j]=max(dp[1,i,j],x+c[i,j])
    return max(dp[:,h,w])
if sys.argv[-1]=='ONLINE_JUDGE':
  from numba.pycc import CC
  cc=CC('my_module')
  cc.export('main','i8(i8,i8,i8,i8[:,:])')(main)
  cc.compile()
  exit()
from my_module import main
(h,w,k),*t=[int_(t.split())for t in open(0)]
print(main(h,w,k,int_(t)))