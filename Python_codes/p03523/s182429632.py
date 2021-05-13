'''
Created on 2020/08/19

@author: harurun
'''
def main():
  import re
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write
  
  S=pin()[:-1]
  if re.fullmatch("A{0,1}KIHA{0,1}BA{0,1}RA{0,1}",S)==None:
    print("NO")
  else:
    print("YES")
  return 

main()