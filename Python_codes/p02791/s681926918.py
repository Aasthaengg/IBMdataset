'''
Created on 2020/08/17

@author: harurun
'''
def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write

  N=int(pin())
  P=list(map(int,pin().split()))
  ans=0
  m=P[0]
  for i in range(N):
    if m>=P[i]:
      m=P[i]
      ans+=1
  print(ans)
  return 

main()