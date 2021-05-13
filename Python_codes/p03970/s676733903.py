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
  ans=0
  T="CODEFESTIVAL2016"
  for i in range(16):
    if S[i]==T[i]:
      continue
    ans+=1
  print(ans)
  return 

main()