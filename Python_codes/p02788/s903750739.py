import sys
f=lambda:map(int,sys.stdin.readline().split())
n,d,a=f()
lt=sorted(tuple(f()) for _ in range(n))
from collections import *
q=deque()
c=s=0
for x,h in lt:
  while q and q[0][0]<x: s+=q.popleft()[1]
  h-=s
  if h<1: continue 
  t=-h//a; c-=t; s-=t*a; q.append((x+d*2,t*a))
print(c)