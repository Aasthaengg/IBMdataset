H,W=map(int,input().split())
N=int(input())
A=list(map(int,input().split()))
G=[[0]*W for i in range(H)]
import numpy
from bisect import bisect_right
w=numpy.cumsum(A)
count=0
for i in range(H):
  if i%2==0:
    a=0
    b=W
    c=1
  else:
    a=W-1
    b=-1
    c=-1
  for j in range(a,b,c):
    G[i][j]=bisect_right(w,count)+1
    count+=1
  print(*G[i])