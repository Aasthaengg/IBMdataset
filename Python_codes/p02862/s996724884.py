import sys
input=sys.stdin.readline
from itertools import combinations

X,Y=(int(x) for x in input().rstrip('\n').split())
if (X+Y) % 3 != 0:
  print(0)
else:
  t = (X+Y)//3
  if X<t or Y<t:
    print(0)
  else:
    s = abs(X-Y)
    if s==t:
      print(1)
    else:
      a = (t-s) // 2      
      res = t
      for i in range(1,a):
        res = res*(t-i)
        ad = pow(i+1,1000000005,1000000007)%1000000007
        res = res*ad
        res = res%1000000007
      print(res%1000000007)