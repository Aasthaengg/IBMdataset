n,k=(int(i) for i in input().strip().split(" "))
ar=[int(i) for i in input().strip().split(" ")]
from math import ceil
pos=ar.index(1)
a=n-1-pos
b=pos
a1=(a//(k-1))
a2=b//(k-1)
c=ceil((n-1-((a1+a2)*(k-1)))/(k-1))
print(a1+a2+c)


