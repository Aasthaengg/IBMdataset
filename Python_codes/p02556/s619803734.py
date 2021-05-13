'''
Created on 2020/09/14

@author: harurun
'''
def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write

  N=int(pin())
  x,y=map(int,pin().split())
  z1=x+y
  z2=x+y
  w1=x-y
  w2=x-y
  for i in range(N-1):
    x,y=map(int,pin().split())
    z1=max(z1,x+y)
    z2=min(z2,x+y)
    w1=max(w1,x-y)
    w2=min(w2,x-y)
  print(max(z1-z2,w1-w2))
  return
main()
#解説AC