n=int(input())
x=list(map(int,list(input())))
def popcount(x):
  ret=0
  while x:
    if x%2==1:ret+=1
    x//=2
  return ret
def f(x):
  ret=0
  while x:
    x%=popcount(x)
    ret+=1
  return ret
from collections import Counter
xpop=Counter(x)[1]
xint_mi,xint_pl=0,0

for i,y in enumerate(x):
  if xpop>1:
    xint_mi+=(pow(2,n-i-1,xpop-1)*y)%(xpop-1)
    xint_mi%=(xpop-1)
  xint_pl+=(pow(2,n-i-1,xpop+1)*y)%(xpop+1)
  xint_pl%=(xpop+1)

for i,y in enumerate(x):
  if y and xpop>1:
    yint=xint_mi-pow(2,n-i-1,xpop-1)
    ypop=xpop-1
  else:
    yint=xint_pl+pow(2,n-i-1,xpop+1)
    ypop=xpop+1
  if y==1 and xpop==1:
    print(0)
    continue
  yint%=ypop
  #print(yint,ypop)
  print(f(yint)+1)
