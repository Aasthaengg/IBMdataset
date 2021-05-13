'''
Created on 2020/08/20

@author: harurun
'''
def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write
  
  A,B,C=map(int,pin().split())
  if A==B and B==C:
    print("Yes")
    return 
  print("No")
  return 

main()