'''
Created on 2020/08/20

@author: harurun
'''
def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write
  
  N=int(pin())
  ans=0
  pre=0
  for _ in [0]*N:
    A,B=map(int,pin().split())
    if ans<A:
      ans=A 
      pre=B 
  print(ans+pre)
  return 

main()