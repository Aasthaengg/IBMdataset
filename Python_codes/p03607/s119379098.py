from collections import defaultdict
import sys
n=int(input())
a=list(map(int,sys.stdin.read().split()))
a.sort()
curc=0
cntc=0
ans=0
for aa in a:
  if aa == curc:
    cntc+=1
  else:
    curc=aa
    ans+=cntc%2
    cntc=1
ans+=cntc%2
print(ans)
