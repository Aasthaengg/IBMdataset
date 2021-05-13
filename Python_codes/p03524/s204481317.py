'''
Created on 2020/08/28

@author: harurun
'''
def main():
  import collections
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write
  
  S=pin()[:-1]
  a=0
  b=0
  c=0
  for i in S:
    if i=="a":
      a+=1
    elif i=="b":
      b+=1
    else:
      c+=1
  if max(a,b,c)-min(a,b,c)<=1:
    print("YES")
  else:
    print("NO")
  return 
main()
#解説AC