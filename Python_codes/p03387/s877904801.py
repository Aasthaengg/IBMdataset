'''
Created on 2020/08/17

@author: harurun
'''
def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write
  
  A=list(map(int,pin().split()))
  A.sort()
  t=A[2]
  ans=0
  if A[0]%2!=A[1]%2:
    ans+=1
    A[1]+=1
    A[2]+=1
  ans+=A[2]-A[1]+(A[1]-A[0])//2
  print(ans)
  return 

main()