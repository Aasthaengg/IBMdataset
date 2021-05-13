'''
Created on 2020/09/08

@author: harurun
'''
def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write

  N,M,K=map(int,pin().split())
  for i in range(N+1):
    for j in range(M+1):
      if i*(M-j)+(N-i)*j==K:
        print("Yes")
        return
  print("No")
  return
main()