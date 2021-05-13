'''
Created on 2020/09/03

@author: harurun
'''
def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write
  
  N=int(pin())
  A=1
  B=N-A
  m=10**9
  for i in range(N-1):
    f=0
    for j in str(A):
      f+=int(j)
    for k in str(B):
      f+=int(k)
    m=min(m,f)
    A+=1
    B-=1
  print(m)
  return 
main()