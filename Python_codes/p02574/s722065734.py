import math
n=int(input())
a=list(map(int,input().split()))
A=max(a)
l=[i for i in range(A+1)]
for i in range(2,A+1):
  if l[i]==i:
    for j in range(1,A//i+1):
      if i*j<=A:
        l[i*j]=i

L=set()
f=0
for i in range(n):
  x=a[i]
  L2=set()
  while x!=1:
    L2.add(l[x])
    x//=l[x]
  L2=list(L2)
  for j in range(len(L2)):
    if L2[j] in L:
      f=1
    else:
      L.add(L2[j])
  if f==1:
    break
if f==0:
  print('pairwise coprime')
  exit()

y=a[0]
for i in range(1,n):
  y=math.gcd(y,a[i])
if y==1:
  print('setwise coprime')
else:
  print('not coprime')