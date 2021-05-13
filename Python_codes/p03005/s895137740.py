'''
Created on 2020/08/20

@author: harurun
'''
def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write
  
  N,K=map(int,pin().split())
  if K==1:
    print(0)
    return 
  t=N-K 
  print(t)
  return 

main()