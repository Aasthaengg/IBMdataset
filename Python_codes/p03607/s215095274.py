n=int(input())
from collections import Counter
c=Counter()
for i in range(n):
  aa=int(input())
  if c[aa]>0:
    c[aa]-=1
    continue
  else:
    c[aa]+=1
ans=0
for k,v in c.items():
  if v>0:ans+=1
print(ans)
