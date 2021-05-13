'''
Created on 2020/08/21

@author: harurun
'''
def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write
  
  l=[0]*4
  for i in range(3):
    a,b=map(int,pin().split())
    l[a-1]+=1
    l[b-1]+=1
  t=sorted(list(set(l)))
  if t==[1,2]:
    print("YES")
  else:
    print("NO")
  return 

main()