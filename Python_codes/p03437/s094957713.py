'''
Created on 2020/08/20

@author: harurun
'''
def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write
  
  X,Y=map(int,pin().split())
  if X%Y==0:
    print(-1)
    return 
  print(X)
  return 

main()