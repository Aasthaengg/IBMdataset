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
  A=list(map(int,pin().split()))
  cnt=0
  for i in A:
    if i%2==1:
      cnt+=1
  if cnt%2==0:
    print("YES")
  else:
    print("NO")
  return 

main()