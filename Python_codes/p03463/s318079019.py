'''
Created on 2020/08/21

@author: harurun
'''
def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write
  
  N,A,B=map(int,pin().split())
  t=B-A-1
  if t%2==0:
    print("Borys")
  else:
    print("Alice")
  return 
main()