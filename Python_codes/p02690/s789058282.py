import numpy as np

X=int(input())
ans=[0,0]

for i in range(-120,120):
  a=i
  for j in range(-120 , 120):
    b=j
    if (a**5 - b**5) ==X:
      ans[0]=a
      ans[1]=b

print("{} {}".format(ans[0],ans[1]))