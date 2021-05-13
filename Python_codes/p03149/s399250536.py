'''
Created on 2020/08/20

@author: harurun
'''
def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write
  
  S=list(pin().split())
  T="".join(S)
  if T.count("1")==1 and T.count("9")==1 and T.count("7")==1 and T.count("4")==1:
    print("YES")
    return 
  print("NO")
  return 

main()