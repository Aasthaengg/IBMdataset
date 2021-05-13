import sys
from collections import defaultdict

_,*s=sys.stdin.read().split()
intl=defaultdict(int)
for p in s:
  intl[p[0]]+=1

march=list(intl[w] for w in 'MARCH')
ans=0
for i in range(5):
  for j in range(i+1,5):
    for k in range(j+1,5):
      ans+=march[i]*march[j]*march[k]
print(ans)