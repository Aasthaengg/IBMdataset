import sys
from collections import Counter

read=sys.stdin.read

n,*a=map(int,read().split())
ca=Counter(a)
ans=0
for x in iter(ca):
  if ca[x]<x:
    ans+=ca[x]
  elif ca[x]>x:
    ans+=ca[x]-x
print(ans)
