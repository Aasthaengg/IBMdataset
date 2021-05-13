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
  if X==1 and Y==1:
    print(1000000)
  else:
    R=[3,2,1]+[0]*205
    print((R[X-1]+R[Y-1])*100000)
  return

main()