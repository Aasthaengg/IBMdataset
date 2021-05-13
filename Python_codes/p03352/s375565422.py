import math
x=int(input())
lis=[1]
for i in range(2,math.ceil(math.sqrt(x))):
  n=i*i
  while n<=x:
    lis.append(n)
    n*=i

print(max(lis))