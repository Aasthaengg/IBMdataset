'''
Created on 2020/08/21

@author: harurun
'''
def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write
  
  A,B,K=map(int,pin().split())
  for i in range(K):
    if i%2==0:
      if A%2==1:
        A-=1
      A=A//2
      B+=A
    else:
      if B%2==1:
        B-=1
      B=B//2
      A+=B 
  print(f"{A} {B}")
  return 
main()