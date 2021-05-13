import math

s,c=map(int,input().split())

if s*2>c:
  print(int(c/2))

else:
  count=s
  c-=s*2
  count+=math.floor(c/4)
  print(count)