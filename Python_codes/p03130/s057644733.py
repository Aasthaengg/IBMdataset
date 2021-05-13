x=[]
for i in range(3):
  a,b=input().split()
  x.append(a)
  x.append(b)
from collections import Counter as co
d=sorted(list(co(x).values()))
print('YES' if d==[1,1,2,2] else 'NO')