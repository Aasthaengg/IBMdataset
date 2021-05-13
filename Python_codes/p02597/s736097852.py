'''
Created on 2020/08/22

@author: harurun
'''
def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write
  
  N=int(pin())
  c=pin()[:-1]
  r=0
  w=0
  for i in c:
    if i=="R":
      r+=1
    else:
      w+=1
#  if r==N or w==N:
#    print(0)
#    return 
  nL=0
  nR=r 
  num=max(nL,nR)
  for i in c:
    if i=="R":
      nR-=1
    else:
      nL+=1
    if num>max(nL,nR):
      num=max(nL,nR)
  print(num)
  return 
main()
#解説AC