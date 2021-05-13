'''
Created on 2020/09/02

@author: harurun
'''
def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write

  N=int(pin())
  A=list(map(int,pin().split()))
  cnt=0
  for i in A:
    if i%2==0:
      cnt+=1
  print(3**N-2**cnt)
  return
main()
#解説AC