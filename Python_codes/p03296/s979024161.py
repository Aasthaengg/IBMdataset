'''
Created on 2020/08/21

@author: harurun
'''
def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write

  N=int(pin())
  a=list(map(int,pin().split()))
  cnt=0
  before=0
  for i in a:
    if before==i:
      before=0
      cnt+=1
    else:
      before=i
  print(cnt)
  return
main()