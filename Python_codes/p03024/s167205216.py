'''
Created on 2020/09/06

@author: harurun
'''
def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write
  
  S=pin()[:-1]
  t=S.count("o")
  u=len(S)
  if 15-u+t>=8:
    print("YES")
  else:
    print("NO")
  return 
main()