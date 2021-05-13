import math
k = int(input())
a = list(map(int,input().split()))
ar = list(reversed(a))
syou = 0
for i in ar:
  if syou > i:
    l = math.ceil(syou/i)
    syou = l * i
  else:
    syou = i
dai = 0
for i in ar:
  if dai > i:
    l = math.ceil(dai/i)
    if dai == l * i:
      dai = l* i + i -1
    else:
      dai = max(l * i -1,dai)
  else:
    dai = i + i -1
kaku = syou + 0
for i in a:
  kaku = (kaku//i) *i
if kaku ==2:
  print(syou,dai)
else:
  print(-1)