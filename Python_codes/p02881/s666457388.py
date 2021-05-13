import math
n=int(input())
x=math.floor(math.sqrt(n))
while True:
  if n % x==0:
    print((x+n//x)-2)
    break
  x-=1
