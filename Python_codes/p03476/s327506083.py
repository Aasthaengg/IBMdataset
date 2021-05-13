def sieve(x):
  p=[]
  b=[1]*x
  for i in range(2,x):
    if b[i]:
      p+=[i]
      for j in range(2*i,x,i): b[j]=0
  return p
p=sieve(10**5+1)
s=set(i for i in p if i<5e4)
l=[0]*(10**5)
for i in p[1:]:
  if i//2+1 in s:
    l[i]=1
from itertools import *
S=[*accumulate(l)]
q=int(input())
for _ in range(q):
  l,r=map(int,input().split())
  print(S[r]-S[l-1])