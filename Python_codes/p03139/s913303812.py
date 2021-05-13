'''
Created on 2020/08/20

@author: harurun
'''
def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write
  
  N,A,B=map(int,pin().split())
  t=0
  if N<=A+B:
    t=abs(N-A-B)
  print(f"{min(A,B)} {t}")
  return 

main()  