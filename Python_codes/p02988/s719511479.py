n=int(input())
a=[0]*n
a[:]=map(int,input().split())
r=0
import copy
for ii in range(n-2):
  b=copy.copy(a[ii:ii+3])
  c=copy.copy(b)
  b.sort()
  if b[1]==c[1]:
    r+=1
print(r)