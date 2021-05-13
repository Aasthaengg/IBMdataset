import copy
import math
c=[0]*(10**5+1)
for n in range(2,10**5+1):
  for k in range(2, int(math.sqrt(n))+1):
    if n%k==0:
      break
  else:
    c[n]=1
cc=[0]*(10**5+1)
for n in range(1,10**5+1,2):
  if c[n] and c[(n+1)//2]:
    cc[n]=1
#print(*c[:100])
for i in range(1,10**5+1):
  cc[i] += cc[i-1]
#print(*c[:100])
#print(*[(i,cc[i]) for i in range(1,54)])
q=int(input())
for i in range(q):
  l,r=map(int,input().split())
  print(cc[r]-cc[l-1])