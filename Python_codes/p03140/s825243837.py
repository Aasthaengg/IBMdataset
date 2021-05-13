'''
Created on 2020/08/21

@author: harurun
'''
def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write
  
  N=int(pin())
  A=pin()[:-1]
  B=pin()[:-1]
  C=pin()[:-1]
  ans=0
  for i in range(N):
    l=[A[i],B[i],C[i]]
    t=len(list(set(l)))
    ans+=t-1
  print(ans)
  return 
main()