x=int(input())
l=x//11
cnt=2*l
if x%11==0:
  print(cnt)
elif 0<x%11<=6:
  print(cnt+1)
else:
  print(cnt+2)