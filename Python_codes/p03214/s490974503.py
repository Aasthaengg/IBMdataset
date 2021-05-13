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
  ave=sum(a)
  ans=0
  now=100*N
  for i in range(N):
    if abs(N*a[i]-ave)<now:
      now=abs(N*a[i]-ave)
      ans=i 
  print(ans)
  return 
main()