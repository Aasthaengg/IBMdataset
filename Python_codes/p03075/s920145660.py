import math
a=[int(input()) for i in range(5)]
b=int(input())
count=0
for i in a:
  for j in a:
    if math.fabs(i-j)>b:
      count+=1
    else:
      continue
if count!=0:
  print(':(')
else:
  print('Yay!')