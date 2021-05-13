'''
Created on 2020/09/03

@author: harurun
'''
def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write
  
  N,K=map(int,pin().split())
  print(N-K+1)
  return 
main()