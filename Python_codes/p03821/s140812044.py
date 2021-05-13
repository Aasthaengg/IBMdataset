'''
Created on 2020/08/28

@author: harurun
'''
def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write
  
  N=int(pin())
  A=[]
  B=[]
  for _ in [0]*N:
    a,b=map(int,pin().split())
    A.append(a)
    B.append(b)
  m=0
  for j in range(1,N+1):
    t=(A[-j]+m)%B[-j]
    if t!=0:
      m+=B[-j]-t
  print(m)
  return 
main()
