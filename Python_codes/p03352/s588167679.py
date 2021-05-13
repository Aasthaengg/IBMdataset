import math
x=int(input())
l=[1]
for i in range(2,int(math.sqrt(x))+1):
  p=i
  while 1:
    p*=i
    if p<=x:
      l.append(p)
    else:
      break
l.sort()
print(l[-1])