'''
Created on 2020/08/20

@author: harurun
'''
def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write
  
  N,K=map(int,pin().split())
  t=0
  if N%2==0:
    t=N//2
  else:
    t=N//2+1
  if t>=K:
    print("YES")
    return 
  print("NO")
  return 

main()