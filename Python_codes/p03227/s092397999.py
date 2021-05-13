'''
Created on 2020/08/20

@author: harurun
'''
def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write
  
  S=pin()[:-1]
  if len(S)==2:
    print(S)
    return 
  print(S[::-1])
  return 

main()