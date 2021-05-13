'''
Created on 2020/09/03

@author: harurun
'''
def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write
  
  N,A,B=map(int,pin().split())
  if (B-A)%2==0:
    print((B-A)//2)
    return 
  if A<N-B+1:
    print(A+(B-A-1)//2)
  else:
    print(N-B+1+(B-A-1)//2)
  return 
main()