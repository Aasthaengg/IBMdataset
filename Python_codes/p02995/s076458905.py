'''
Created on 2020/08/28

@author: harurun
'''

def lcm(a,b):
  import math
  return a*b//math.gcd(a,b)

def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write
  
  A,B,C,D=map(int,pin().split())
  M=B//C+B//D-B//lcm(C,D)
  m=(A-1)//C+(A-1)//D-(A-1)//lcm(C,D)
  t=M-m 
  print(B-A+1-t)
  return 
main()