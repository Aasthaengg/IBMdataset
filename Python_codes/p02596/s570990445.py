'''
Created on 2020/08/22

@author: harurun
'''
def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write
  
  K=int(pin())
  a=7%K
  for i in range(K):
    if a%K==0:
      print(i+1)
      break
    a=(10*a+7)%K
  else:
    print(-1)
  return 
main()

#解説AC