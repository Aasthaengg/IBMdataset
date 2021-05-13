a,b,c,d,e,f=map(int,input().split())
able_water=[]
for na in range(1+f//(a*100)):
  for nb in range(1+(f-na*a*100)//(b*100)):
    water=na*a*100+nb*b*100
    if water and water<=f:
      able_water.append(water)
able_water.sort()
import bisect
from fractions import Fraction
ans=[0,0,0]
max_s=(f*e+100-1)//100
for nd in range(1+max_s//d):
  for nc in range(1+(max_s-nd*d)//c):
    sugger=nc*c+nd*d
    min_water=(sugger*100+e-1)//e
    if min_water+sugger>f:continue
    idx=bisect.bisect_left(able_water,min_water)
    if idx <len(able_water) and able_water[idx]+sugger<=f:
      if ans[0]<=Fraction(sugger,(able_water[idx]+sugger)):
        ans=[Fraction(sugger,(able_water[idx]+sugger)),able_water[idx]+sugger,sugger]
print(ans[1],ans[2])