def i1():
 return int(input())
def i2():
 return [int(i) for i in input().split()]

a=list(input())
from collections import Counter
c= Counter(a)
cv=list(c.values())
s=len(a)*(len(a)-1)/2
for i in cv:
 s-=i*(i-1)/2
print(int(s)+1)