import sys
from copy import deepcopy
input = sys.stdin.readline
n,m=map(int,input().split())
d=[[100000]*n for _ in range(n)]
a=[0]*m
b=[0]*m
c=[0]*m
for i in range(m):
  a0,b0,c0=map(int,input().split())
  a[i]=a0-1
  b[i]=b0-1
  c[i]=c0
  d[a0-1][b0-1]=c0
  d[b0-1][a0-1]=c0
for i in range(n):
  d[i][i]=0
d2=deepcopy(d)
for k in range(n):
  for i in range(n):
    for j in range(n):
      d[i][j]=min(d[i][j],d[i][k]+d[k][j])
count=0
for i in range(n):
  for j in range(i):
    if d2[i][j] != 100000 and d[i][j]!=d2[i][j]:
      count+=1
print(count)
