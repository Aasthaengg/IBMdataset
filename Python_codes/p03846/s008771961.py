import sys
from collections import defaultdict
MOD=10**9+7
N=int(input())
alist=list(map(int,input().split()))

adic=defaultdict(int)
for a in alist:
  adic[a]+=1
#print(adic)

answer=1
if N%2==1:  
  for a,v in adic.items():
    #print(a,v)
    if a==0:
      if v!=1:
        print(0)
        sys.exit(0)
    elif a%2==0:
      if v!=2:
        print(0)
        sys.exit(0)
      else:
        answer*=2
        answer%=MOD
    else:
      print(0)
      sys.exit(0)
  print(answer)
else:
  for a,v in adic.items():
    #print(a,v)
    if a%2==0:
      print(0)
      sys.exit(0)
    else:
      if v==2:
        answer*=2
        answer%=MOD
      else:
        print(0)
        sys.exit(0)
  print(answer)