n=int(input())
from collections import defaultdict
d=defaultdict(int)

for i in range(1,n+1):
  d[str(i)[0]+str(i)[-1]]+=1

sm=0
for i in range(1,10):
  for j in range(1,10):
    sm+=d[str(i)+str(j)]*d[str(j)+str(i)]
print(sm)