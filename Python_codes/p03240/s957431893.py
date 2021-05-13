n=int(input())
info=[]
import sys
for i in range(n):
  x,y,h=map(int,input().split())
  info.append([x,y,h])
for x in range(0,101):
  for y in range(0,101):
    for A in info:
      if A[2]!=0:
        h=A[2]+abs(x-A[0])+abs(y-A[1])
        break
    failflag=0
    for A in info:
      if A[2]!=max(0,h-abs(x-A[0])-abs(y-A[1])):
        failflag=1
        break
    if failflag==0:
      print(x)
      print(y)
      print(h)
      sys.exit()