from collections import defaultdict
import sys
n=int(input())
a=list(map(int,sys.stdin.read().split()))
dd=defaultdict(lambda: 0)
for aa in a:
  dd[aa]+=1
ans=0
for e in dd.values():
  if e%2==1:
    ans+=1
print(ans)
