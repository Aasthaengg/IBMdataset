'''
Created on 2020/08/20

@author: harurun
'''
def main():
  import re
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write

  s=pin()[:-1]
  if re.fullmatch(r"[A-Z]*C+[A-Z]*F+[A-Z]*", s)==None:
    print("No")
    return
  print("Yes")
  return

main()